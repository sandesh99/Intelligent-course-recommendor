import openai
import numpy as np
import config

openai.api_key = config.OPENAI_API_KEY
embedding_model = config.EMBEDDING_MODEL

def get_embedding(text: str):
    # fetch embedding from OpenAI
    res = openai.embeddings.create(model=embedding_model, input=text)
    return np.array(res.data[0].embedding, dtype=np.float32)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
