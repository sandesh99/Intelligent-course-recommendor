from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
import os
import config


def load_or_create_chroma(kb_path=config.KB_PATH, chroma_db_path=config.CHROMA_DB_PATH):
    """Load existing Chroma DB if available, else create a new one."""
    embeddings = OpenAIEmbeddings(model=config.EMBEDDING_MODEL)

    if os.path.exists(chroma_db_path) and os.listdir(chroma_db_path):
        print(f"[INFO] Loading existing Chroma DB from {chroma_db_path}")
        db = Chroma(persist_directory=chroma_db_path, embedding_function=embeddings)
    else:
        print("[INFO] Creating new Chroma DB...")
        loader = DirectoryLoader(kb_path, glob="*.md")
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, chunk_overlap=50
        )
        split_docs = splitter.split_documents(docs)

        db = Chroma.from_documents(split_docs, embeddings, persist_directory=chroma_db_path)
        db.persist()
        print(f"[INFO] Saved Chroma DB to {chroma_db_path}")

    return db


def build_qa_chain(db):
    retriever = db.as_retriever()
    llm = ChatOpenAI(model_name=config.CHAT_MODEL, temperature=0)

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )


def get_answer(question, user_profile=None, kb_path=config.KB_PATH, chroma_db_path=config.CHROMA_DB_PATH):
    """Get an answer for the given question."""
    db = load_or_create_chroma(kb_path, chroma_db_path)
    qa_chain = build_qa_chain(db)

    context = f"User profile: {user_profile}" if user_profile else ""
    query = f"{context}\n\nQuestion: {question}"

    return qa_chain.run(query)
