# JSON-CSV Converter

A tiny command-line tool to convert between **JSON**, **CSV**, and optionally **Excel (XLSX)**.  
Perfect for quick data transformations without opening spreadsheets or writing custom scripts.

---

## ✨ Features
- Convert **JSON → CSV**
- Convert **CSV → JSON**
- (Optional) **JSON → XLSX** export
- Fast, minimal, and easy to use (Python + pandas)

---

## 📁 Project Structure

```
JSON-converter/
├─ converter.py
├─ requirements.txt
├─ README.md
└─ examples/
   ├─ sample.json
   └─ sample.csv
```

> You can rename the folder however you like (e.g., `json-csv-converter`).  
> If you rename the script file, remember to run the new name (e.g., `python data_converter.py ...`).

---

## 🧰 Requirements
- Python 3.8+
- `pandas`
- `openpyxl` (only if exporting to XLSX)

Install dependencies:
```bash
pip install -r requirements.txt
```

> Tip: Use a virtual environment for a clean setup:
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
> ```

---

## 🚀 Usage

Basic command:
```bash
python converter.py --input <path/to/input> --output <path/to/output> --to <csv|json|xlsx>
```

Examples:
```bash
# JSON → CSV
python converter.py --input examples/sample.json --output examples/sample.csv --to csv

# CSV → JSON
python converter.py --input examples/sample.csv --output examples/sample.json --to json

# JSON → XLSX (requires openpyxl)
python converter.py --input examples/sample.json --output examples/sample.xlsx --to xlsx
```

Arguments:
- `--input` / `-i`  : Path to the input file  
- `--output` / `-o` : Path to the output file  
- `--to` / `-t`     : Target format (`csv`, `json`, or `xlsx`)

---

## 🧪 Sample Data

`examples/sample.json`
```json
[
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 30}
]
```

Run:
```bash
python converter.py --input examples/sample.json --output examples/sample.csv --to csv
```

---

## ❓ Troubleshooting

- **`Command 'python' not found`**  
  Use `python3`, or install the `python-is-python3` package on your distro.

- **Module not found: `pandas`**  
  You’re likely outside your virtual environment. Activate it:
  ```bash
  source .venv/bin/activate
  ```
  Then reinstall:
  ```bash
  pip install -r requirements.txt
  ```

- **Encoding issues with CSV**  
  Ensure your CSV is UTF-8 encoded. You can try re-saving with UTF-8 in your editor.

---

## 🪪 License
MIT License — feel free to use and modify.
