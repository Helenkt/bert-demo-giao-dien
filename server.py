import argparse
import json
import mimetypes
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent
DEFAULT_MODEL_DIR = ROOT / "models" / "bert-small-en"
DEFAULT_MODEL_NAME = "google/bert_uncased_L-4_H-256_A-4"


class BertRuntime:
    def __init__(self, model_arg: str, allow_download: bool):
        self.model_arg = model_arg
        self.allow_download = allow_download
        self._pipeline = None
        self._model_label = model_arg

    def status(self):
        try:
            import transformers  # noqa: F401
            import torch  # noqa: F401
            packages_ok = True
        except Exception as exc:
            return {
                "backend": True,
                "ready": False,
                "packages_ok": False,
                "model": self._model_label,
                "error": f"Missing Python package: {exc}",
            }

        model_path = Path(self.model_arg)
        local_model_ready = model_path.exists()
        return {
            "backend": True,
            "ready": packages_ok and (local_model_ready or self.allow_download),
            "packages_ok": packages_ok,
            "model": self._model_label,
            "local_model_ready": local_model_ready,
            "allow_download": self.allow_download,
        }

    def load(self):
        if self._pipeline is not None:
            return self._pipeline

        from transformers import AutoModelForMaskedLM, AutoTokenizer, pipeline

        local_files_only = not self.allow_download
        tokenizer = AutoTokenizer.from_pretrained(self.model_arg, local_files_only=local_files_only)
        model = AutoModelForMaskedLM.from_pretrained(self.model_arg, local_files_only=local_files_only)
        self._pipeline = pipeline("fill-mask", model=model, tokenizer=tokenizer, top_k=5)
        return self._pipeline

    def fill_mask(self, text: str):
        if "[MASK]" not in text:
            raise ValueError("Cau dau vao can co [MASK].")

        pipe = self.load()
        outputs = pipe(text)
        predictions = []
        for item in outputs:
            token = item.get("token_str", "").strip()
            predictions.append(
                {
                    "word": token,
                    "score": round(float(item.get("score", 0.0)) * 100, 2),
                    "sequence": item.get("sequence", ""),
                }
            )
        return {
            "real": True,
            "task": "fill-mask",
            "model": self._model_label,
            "input": text,
            "predictions": predictions,
        }


class Handler(SimpleHTTPRequestHandler):
    bert_runtime: BertRuntime = None

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self.send_response(302)
            self.send_header("Location", "/outputs/bert_demo_giao_dien.html")
            self.end_headers()
            return
        if self.path == "/api/status":
            self.write_json(self.bert_runtime.status())
            return
        return self.serve_file()

    def do_POST(self):
        if self.path == "/api/fill-mask":
            self.handle_fill_mask()
            return
        self.send_error(404, "Not found")

    def handle_fill_mask(self):
        try:
            payload = self.read_json()
            text = str(payload.get("text", "")).strip()
            result = self.bert_runtime.fill_mask(text)
            self.write_json(result)
        except Exception as exc:
            self.write_json({"real": False, "error": str(exc)}, status=400)

    def read_json(self):
        length = int(self.headers.get("Content-Length", "0"))
        data = self.rfile.read(length)
        if not data:
            return {}
        return json.loads(data.decode("utf-8"))

    def write_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def serve_file(self):
        raw_path = unquote(self.path.split("?", 1)[0]).lstrip("/")
        file_path = (ROOT / raw_path).resolve()
        if not str(file_path).startswith(str(ROOT)) or not file_path.is_file():
            self.send_error(404, "File not found")
            return

        content_type = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
        data = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def parse_args():
    parser = argparse.ArgumentParser(description="Run BERT demo server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument(
        "--model",
        default=str(DEFAULT_MODEL_DIR if DEFAULT_MODEL_DIR.exists() else DEFAULT_MODEL_NAME),
        help="Local model directory or Hugging Face model id.",
    )
    parser.add_argument(
        "--allow-download",
        action="store_true",
        help="Allow transformers to download model files if the model is not available locally.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    Handler.bert_runtime = BertRuntime(args.model, args.allow_download)
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Serving BERT demo at http://{args.host}:{args.port}/outputs/bert_demo_giao_dien.html")
    print(f"Model: {args.model}")
    print("Press Ctrl+C to stop.")
    server.serve_forever()


if __name__ == "__main__":
    main()
