# BERT Demo Giao Dien

Du an gom tai lieu thuyet trinh va demo giao dien ve mo hinh BERT.

## File chinh

- `outputs/bert_demo_giao_dien.html`: demo giao dien chay offline tren trinh duyet.
- `outputs/bert_thuyet_trinh.docx`: tai lieu noi dung thuyet trinh ve BERT.

## Cach chay demo offline

Mo truc tiep file:

```text
outputs/bert_demo_giao_dien.html
```

Hoac chay local server trong thu muc du an:

```bash
python -m http.server 8000 --bind 127.0.0.1 -d outputs
```

Sau do mo:

```text
http://127.0.0.1:8000/bert_demo_giao_dien.html
```

## Cach chay BERT that bang Python

Can cai Python truoc. Lan dau chay can co mang de cai thu vien va tai model.

Tren Windows, chay:

```bat
run_bert_server.bat
```

Script nay se:

1. Tao `.venv`
2. Cai `transformers`, `torch`
3. Tai model nho `prajjwal1/bert-tiny` vao `models/bert-tiny`
4. Chay server tai:

```text
http://127.0.0.1:8000/outputs/bert_demo_giao_dien.html
```

Neu da cai thu vien va tai model san, co the chay truc tiep:

```bash
python server.py --model models/bert-tiny
```

Neu muon cho `transformers` tu tai model khi server load lan dau:

```bash
python server.py --model prajjwal1/bert-tiny --allow-download
```

## Ghi chu

Demo HTML van co fallback offline de thuyet trinh chac chan chay duoc. Khi backend Python dang chay, tac vu `[MASK]` se goi BERT that qua endpoint `/api/fill-mask`.

`prajjwal1/bert-tiny` la model BERT nho de demo chay that nhanh hon. Neu can tieng Viet tot hon, co the doi sang `bert-base-multilingual-cased`, nhung model do lon hon nhieu va tai lau hon. Phan phan loai cam xuc va hoi dap muon chay that can model BERT da fine-tune rieng cho tung tac vu.
