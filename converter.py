import argparse
import pandas as pd
import os

def json_to_csv(input_file, output_file):
    df = pd.read_json(input_file)
    df.to_csv(output_file, index=False)
    print(f"[+] Converted {input_file} → {output_file}")

def csv_to_json(input_file, output_file):
    df = pd.read_csv(input_file)
    df.to_json(output_file, orient="records", indent=4)
    print(f"[+] Converted {input_file} → {output_file}")

def json_to_xlsx(input_file, output_file):
    df = pd.read_json(input_file)
    df.to_excel(output_file, index=False)
    print(f"[+] Converted {input_file} → {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert between JSON, CSV, and XLSX formats.")
    parser.add_argument("--input", "-i", required=True, help="Path to input file")
    parser.add_argument("--output", "-o", required=True, help="Path to output file")
    parser.add_argument("--to", "-t", required=True, choices=["json", "csv", "xlsx"], help="Target format")
    
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    target_format = args.to.lower()

    if not os.path.exists(input_file):
        print(f"[!] Input file not found: {input_file}")
        return

    if target_format == "csv":
        json_to_csv(input_file, output_file)
    elif target_format == "json":
        csv_to_json(input_file, output_file)
    elif target_format == "xlsx":
        json_to_xlsx(input_file, output_file)
    else:
        print("[!] Unsupported format")

if __name__ == "__main__":
    main()
