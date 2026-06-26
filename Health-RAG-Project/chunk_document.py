from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

with open("cleaned_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

docs = [Document(page_content=text)]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    with open(f"chunk_{i+1}.txt", "w", encoding="utf-8") as f:
        f.write(chunk.page_content)

print("Chunking completed successfully.")