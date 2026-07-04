# BERT Demo Giao Dien

Du an nay gom tai lieu thuyet trinh va demo giao dien minh hoa cach BERT xu ly ngon ngu tu nhien.

## Noi dung chinh

- `outputs/bert_demo_giao_dien.html`: giao dien demo BERT.
- `outputs/bert_thuyet_trinh.docx`: file noi dung thuyet trinh.
- `server.py`: backend Python de chay BERT that bang `transformers`.
- `setup_bert_demo.bat`: cai thu vien va tai model lan dau.
- `start_bert_demo.bat`: chay server nhanh khi da setup xong.
- `run_bert_server.bat`: script tat-ca-trong-mot tren Windows.

## BERT_NAME

Model dang dung:

```text
BERT Small - google/bert_uncased_L-4_H-256_A-4
```

Day la ban BERT nho, nhe hon BERT base, phu hop de demo tren may ca nhan. Model duoc tai ve thu muc:

```text
models/bert-small-en
```

Thu muc `models/` khong duoc dua len GitHub vi file model kha lon. Nguoi khac clone repo chi can chay `run_bert_server.bat`, script se cai thu vien va tai model neu may chua co.

## Khoi phuc tren may moi hoac sau khi xoa folder

Source code tren GitHub da co du script de tao lai moi thu. Chay:

```bat
git clone https://github.com/Helenkt/bert-demo-giao-dien.git
cd bert-demo-giao-dien
run_bert_server.bat
```

`run_bert_server.bat` se tu dong:

1. Tao moi `.venv`.
2. Cai cac goi trong `requirements.txt`.
3. Tai dung model `google/bert_uncased_L-4_H-256_A-4`.
4. Luu model vao `models/bert-small-en`.
5. Khoi dong Python backend.

Khong dua `.venv/` len Git vi moi truong nay chua duong dan va file nhi phan phu thuoc may. Khong dua `models/` vao Git vi checkpoint co the tai lai tu nguon chinh thuc bang script. Neu can chay hoan toan offline, nen sao luu rieng thu muc `models/bert-small-en` bang file ZIP hoac o luu tru ngoai.

## Cach chay demo nhanh

Lan dau tien, mo terminal trong thu muc du an va chay:

```bat
setup_bert_demo.bat
```

Tu lan sau, chi can chay:

```bat
start_bert_demo.bat
```

Neu muon dung mot lenh de vua setup vua chay server:

```bat
run_bert_server.bat
```

Sau do mo:

```text
http://127.0.0.1:8000/outputs/bert_demo_giao_dien.html
```

Neu da co Python environment va model san, co the chay truc tiep:

```bash
python server.py --model models/bert-small-en
```

Mac dinh `server.py` se tai model truoc khi mo server de luc bam "Chay demo" khong bi cho qua lau. Neu muon mo server truoc roi tai model o lan du doan dau tien:

```bash
python server.py --model models/bert-small-en --lazy
```

## Thu vien can co

```text
transformers
torch
safetensors
```

Co the cai bang:

```bash
pip install -r requirements.txt
```

## Ghi chu

- Tac vu `[MASK]` se goi BERT that qua endpoint `/api/fill-mask` khi backend Python dang chay.
- Backend tra ve token WordPiece that, token id va thong tin kien truc nho cua model de giao dien minh hoa dung hon.
- Tac vu `[MASK]` chi tra ket qua khi backend BERT that dang chay; khong dung ket qua mo phong.
- Phan cam xuc va hoi dap trong demo la minh hoa giao dien. Muon chay that hai tac vu nay can model BERT da fine-tune rieng.
- Repo tren GitHub chi luu source code, tai lieu va giao dien. Khong luu `.venv/` va `models/`.
