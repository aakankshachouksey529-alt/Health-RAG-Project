import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Read cleaned text
with open("cleaned_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

metadata_list = []

for i, chunk in enumerate(chunks):
    metadata = {
        "id": i + 1,
        "text": chunk,
        "source": "health_docs",
        "page": 1,
        "section": "general_health",
        "doc_type": "pdf"
    }
    metadata_list.append(metadata)

# Save JSON
with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata_list, f, indent=4)

print("Metadata created successfully.")