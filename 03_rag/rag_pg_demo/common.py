from pathlib import Path
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaEmbeddings

CHAT_MODEL = "qwen3:0.6b"
EMBED_MODEL = "nomic-embed-text"


# def load_documents():
#     text = Path("data/go.txt").read_text(encoding="utf-8")
#     # Simple paragraph chunking keeps this demo dependency-light and transparent.
#     chunks = [p.strip() for p in text.split("\n\n") if p.strip()]
#     return [Document(page_content=c, metadata={"source": "data/go.txt", "chunk": i})
#             for i, c in enumerate(chunks)]

# from pathlib import Path
# from langchain_core.documents import Document  # or your existing Document import

def load_documents(directory: str = "data"):
    documents = []
    for file_path in sorted(Path(directory).glob("*.txt")):
        text = file_path.read_text(encoding="utf-8")
        # Simple paragraph chunking keeps this demo dependency-light and transparent.
        chunks = [p.strip() for p in text.split("\n\n") if p.strip()]
        for i, c in enumerate(chunks):
            documents.append(
                Document(
                    page_content=c,
                    metadata={"source": file_path.as_posix(), "chunk": i},
                )
            )
    return documents

def embeddings():
    return OllamaEmbeddings(model=EMBED_MODEL)


def answer(question: str, docs):
    context = "\n\n".join(
        f"[Chunk {d.metadata.get('chunk', '?')}] {d.page_content}" for d in docs
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a concise software engineering trainer. Answer only from the supplied context. If the answer is not in the context, say: I don't know from the provided documents."),
        ("human", "Context:\n{context}\n\nQuestion: {question}\n/no_think"),
    ])
    llm = ChatOllama(model=CHAT_MODEL, temperature=0)
    response = (prompt | llm).invoke({"context": context, "question": question})
    return response.content
