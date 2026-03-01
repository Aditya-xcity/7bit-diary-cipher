
# ==============================
# 7-BIT DIARY CIPHER (TERMINAL)
# ENCODER + DECODER + MASTER JSON
# ==============================

import os
import json
from datetime import datetime

MASTER_FILE = "master_diary.json"

BLOCK_TABLE = {
    'a':'0000000','e':'0000001','i':'0000010','o':'0000011','u':'0000100',
    'n':'0010000','r':'0010001','s':'0010010','t':'0010011',
    'l':'0010100','d':'0010101','h':'0010110','m':'0010111',
    'y':'0011000','w':'0011001',
    'b':'0100000','c':'0100001','f':'0100010','g':'0100011',
    'k':'0100100','p':'0100101','v':'0100110','j':'0100111',
    'x':'0101000','z':'0101001',
    ' ':'0110000','\n':'0110001',
    '0':'1000000','1':'1000001','2':'1000010','3':'1000011',
    '4':'1000100','5':'1000101','6':'1000110','7':'1000111',
    '8':'1001000','9':'1001001'
}

REVERSE_BLOCK_TABLE = {v: k for k, v in BLOCK_TABLE.items()}


# ==============================
# ENCODE / DECODE
# ==============================

def encode_text(text):
    text = text.lower()
    return "".join(BLOCK_TABLE[ch] for ch in text if ch in BLOCK_TABLE)

def decode_text(binary):
    decoded = ""
    for i in range(0, len(binary), 7):
        block = binary[i:i+7]
        decoded += REVERSE_BLOCK_TABLE.get(block, "")
    return decoded


# ==============================
# MASTER JSON HANDLING
# ==============================

def load_master():
    if not os.path.exists(MASTER_FILE):
        return {"entries": []}
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_master(data):
    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_entry(filename, encoded_text):
    data = load_master()
    entry_id = len(data["entries"]) + 1

    new_entry = {
        "id": entry_id,
        "filename": filename,
        "encoded": encoded_text,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data["entries"].append(new_entry)
    save_master(data)


# ==============================
# FILE OPERATIONS
# ==============================

def encode_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    encoded = encode_text(content)

    os.makedirs("code", exist_ok=True)
    base = os.path.splitext(os.path.basename(path))[0]
    out_path = os.path.join("code", f"{base}_encoded.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(encoded)

    add_entry(base, encoded)
    print(f" Encoded file saved at: {out_path}")
    print(" Entry added to master_diary.json")

def decode_file(path):
    with open(path, "r", encoding="utf-8") as f:
        binary = f.read().strip()

    decoded = decode_text(binary)

    os.makedirs("decoded", exist_ok=True)
    base = os.path.splitext(os.path.basename(path))[0]
    out_path = os.path.join("decoded", f"{base}_decoded.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(decoded)

    print(f" Decoded file saved at: {out_path}")


# ==============================
# MAIN MENU
# ==============================

def main():
    print("\n==== 7-BIT DIARY CIPHER ====")
    print("1. Encode File")
    print("2. Decode File")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        path = input("Enter text file path to encode: ")
        encode_file(path)

    elif choice == "2":
        path = input("Enter encoded file path to decode: ")
        decode_file(path)

    elif choice == "3":
        print("Goodbye ")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
