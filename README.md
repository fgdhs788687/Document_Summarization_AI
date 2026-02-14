# 📄 AI Document Summarizer (Ollama Powered)

An AI-powered document and web summarization tool built using Python and Ollama.

This application allows you to input:

* 📑 PDF files
* 📄 TXT files
* 📊 CSV files
* 🌐 Web URLs

It then automatically extracts the text and generates a concise summary (200 words or less) using a local LLM model via Ollama.

---

## 🚀 Features

* ✅ PDF text extraction using PyPDF2
* ✅ TXT file reading
* ✅ CSV file summarization using Pandas
* ✅ Web scraping using Requests + BeautifulSoup
* ✅ AI-powered summarization using Ollama (gemma3:1b)
* ✅ Summary history saved to `History.html`
* ✅ Continuous input loop until `exit()` is entered

---

## 🛠️ Technologies Used

* Python 3.x
* Ollama
* PyPDF2
* Pandas
* Requests
* BeautifulSoup4

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install dependencies

```bash
pip install requests PyPDF2 pandas beautifulsoup4
```

### 3️⃣ Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the required model:

```bash
ollama pull gemma3:1b
```

---

## ▶️ How to Run

```bash
python your_script_name.py
```

You will see:

```
AI Document Summarization
Supported formats: PDF, TXT, CSV, HTML or web URL
Type exit() to quit
```

Enter:

* A file path (without quotes), example:

```
C:\Users\YourName\Downloads\file.pdf
```

OR

* A website URL:

```
https://example.com
```

---

## 📂 Output

* Summary is printed in the terminal
* Summary history is appended to:

```
History.html
```

* When you type `exit()`, the program:

  * Clears the console
  * Clears `History.html`
  * Exits safely

---

## ⚠️ Notes

* Make sure file paths are not wrapped in quotes.
* Ensure Ollama is running locally.
* Large documents may take longer to summarize.
* Works best with text-based PDFs (not scanned image PDFs).

---

## 🧠 How It Works

1. Detects file type or URL
2. Extracts raw text
3. Sends text to Ollama using:

   ```
   gemma3:1b
   ```
4. Returns a structured summary (≤ 200 words)
5. Saves summary to HTML history file

---

## 🔮 Future Improvements

* Add DOCX support
* Add GUI version (Tkinter)
* Add Streamlit web app interface
* Add multi-language support
* Add keyword extraction
* Add export to PDF

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## ✨ Author

Faiza
Python Developer | AI Enthusiast

