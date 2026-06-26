import fitz
import re
import os

# Your PDF files (correct names + correct paths)
pdf_files = [
    r"C:\Users\Aakanksha\OneDrive\Desktop\python my-first-project\Health-RAG-Project\Health-awareness.pdf",
    r"C:\Users\Aakanksha\OneDrive\Desktop\python my-first-project\Health-RAG-Project\Mental-Health-Report.pdf",
    r"C:\Users\Aakanksha\OneDrive\Desktop\python my-first-project\Health-RAG-Project\WHO-Nutrition-Guidelines.pdf"
]

clean_text = ""

for pdf_path in pdf_files:
    if not os.path.exists(pdf_path):
        print(f"{pdf_path} not found!")
        continue

    print(f"Processing: {pdf_path}")
    doc = fitz.open(pdf_path)

    for page in doc:
        text = page.get_text()

        # Cleaning
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"Page \d+", "", text)
        text = re.sub(r"[^\w\s.,!?()%:/-]", "", text)

        clean_text += text + "\n"

# Save output
with open("cleaned_text.txt", "w", encoding="utf-8") as f:
    f.write(clean_text)

print("\nAll documents cleaned successfully.")