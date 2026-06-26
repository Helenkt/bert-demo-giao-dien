# BERT Demo Giao Dien

Du an gom tai lieu thuyet trinh va demo giao dien ve mo hinh BERT.

## File chinh

- `outputs/bert_demo_giao_dien.html`: demo giao dien chay offline tren trinh duyet.
- `outputs/bert_thuyet_trinh.docx`: tai lieu noi dung thuyet trinh ve BERT.

## Cach chay demo

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

## Ghi chu

Demo hien tai la ban offline mo phong pipeline BERT de thuyet trinh chac chan chay duoc. Neu muon chay BERT that, can them Python, `transformers`, `torch` va model da tai san.
