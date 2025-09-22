# User Guide — JSON-CSV Converter

This guide helps you install and run the converter quickly.

## 1) Install Python
Make sure you have **Python 3.8+**:
```bash
python3 --version
```

## 2) Get the Project
If you downloaded a ZIP, unzip it.  
If you use Git:
```bash
git clone https://github.com/<your-username>/JSON-converter.git
cd JSON-converter
```

## 3) (Recommended) Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4) Install Dependencies
```bash
pip install -r requirements.txt
```

## 5) Run a Conversion
### JSON → CSV
```bash
python converter.py --input examples/sample.json --output examples/sample.csv --to csv
```

### CSV → JSON
```bash
python converter.py --input examples/sample.csv --output examples/sample.json --to json
```

### JSON → XLSX (optional)
```bash
python converter.py --input examples/sample.json --output examples/sample.xlsx --to xlsx
```

## 6) Common Issues
- **`python: command not found`** → try `python3` instead.  
- **`ModuleNotFoundError: No module named 'pandas'`** → activate the venv and run `pip install -r requirements.txt`.  
- **Wrong file paths** → ensure `--input` and `--output` paths exist (use relative or absolute paths).

## 7) Rename Files (If You Want)
- You can rename `converter.py` to whatever you prefer (e.g., `data_converter.py`).  
- After renaming, call it accordingly:
  ```bash
  python data_converter.py --input ... --output ... --to csv
  ```
- You can also rename the project folder freely. No configuration change is required.

Happy converting! 🎉
