import argparse
from pathlib import Path

from transformers import AutoModelForMaskedLM, AutoTokenizer


def parse_args():
    parser = argparse.ArgumentParser(description="Download and cache a BERT fill-mask model.")
    parser.add_argument("--model", default="bert-base-multilingual-cased")
    parser.add_argument("--out", default="models/bert-base-multilingual-cased")
    return parser.parse_args()


def main():
    args = parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForMaskedLM.from_pretrained(args.model)
    tokenizer.save_pretrained(out)
    model.save_pretrained(out)

    print(f"Saved {args.model} to {out.resolve()}")


if __name__ == "__main__":
    main()
