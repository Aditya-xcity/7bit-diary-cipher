# 🗝️ BinaryDiary

A terminal-based diary encryption system built in Python using a custom 7-bit substitution cipher.

BinaryDiary allows you to encode text files into a structured binary format, decode them back into readable text, and maintain a master JSON database of encrypted entries.

---

## 🚀 Features

* Encode text files into a custom 7-bit binary cipher
* Decode binary files back to readable text
* Automatic folder organization:

  * `code/` → Encoded files
  * `decoded/` → Decoded files
* Master encrypted entry tracking via `master_diary.json`
* Timestamped entries
* Clean terminal-based interface
* Modular architecture (optional external `block_table.json`)

---

## 🏗️ Project Structure

```
BinaryDiary/
│
├── main.py
├── block_table.json        # Optional (external cipher table)
├── master_diary.json       # Auto-generated
│
├── code/                   # Encoded output files
└── decoded/                # Decoded output files
```

---

## 🧠 How It Works

### 🔐 Encoding Process

1. Reads a `.txt` file.
2. Converts each supported character into a predefined 7-bit binary block.
3. Saves the encoded output inside the `code/` directory.
4. Stores metadata (filename, encoded text, timestamp) in `master_diary.json`.

---

### 🔓 Decoding Process

1. Reads a binary `.txt` file.
2. Splits the content into 7-bit chunks.
3. Converts each chunk back to its original character.
4. Saves the decoded file inside the `decoded/` directory.

---

## ▶️ Usage

Run the program:

```
python main.py
```

You will see:

```
==== 7-BIT DIARY CIPHER ====
1. Encode File
2. Decode File
3. Exit
```

Follow the prompts to provide the file path.

---

## 📁 Master JSON Structure

`master_diary.json` keeps track of encrypted entries:

```json
{
  "entries": [
    {
      "id": 1,
      "filename": "example",
      "encoded": "00101100000010",
      "timestamp": "2026-03-01 19:45:00"
    }
  ]
}
```

---

## ⚠️ Security Notice

This project uses a substitution cipher for educational purposes.

It is **not cryptographically secure**.

For production-grade security, consider:

* AES encryption
* Password-derived keys
* The `cryptography` Python library

---

## 🔮 Future Improvements

* Password-protected encryption
* Encrypt `master_diary.json`
* Search encrypted entries
* Delete or update stored entries
* Convert into a packaged CLI tool
* Replace substitution cipher with real cryptographic algorithm

---

## 👨‍💻 Author

Aditya Bhardwaj
B.Tech – Computer Science Engineering

---

## 📜 License

This project is intended for educational and personal use.
