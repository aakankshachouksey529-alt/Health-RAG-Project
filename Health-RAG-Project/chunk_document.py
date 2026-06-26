from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# Read cleaned text
with open("cleaned_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Create document
docs = [Document(page_content=text)]

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

# Store chunks in a Python list
chunk_texts = [chunk.page_content for chunk in chunks]

# Show result
print(f"Total Chunks: {len(chunk_texts)}")
print("Chunking completed successfully.")

# Preview first chunk
print("\nFirst Chunk Preview:\n")
print(chunk_texts[0][:500])