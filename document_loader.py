# document_loader.py
import fitz  # PyMuPDF

def load_text(doc_bytes, filename="file.pdf"):
    if filename.endswith(".txt"):
        return doc_bytes.decode("utf-8")
    elif filename.endswith(".pdf"):
        doc = fitz.open(stream=doc_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    else:
        raise ValueError("Unsupported file type.")

def extract_text(path):
    with open(path, "rb") as f:
        return load_text(f.read(), path)
