import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Models used
EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"

# data paths
COURSE_DATA_PATH = "data/courses.json"
FEEDBACK_DATA_PATH = "data/feedback.json"
KB_PATH = "data/knowledge_base"
CHROMA_DB_PATH = "data/chroma_db"
