from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_sentences(sentences):
    embeddings = []
    for sentence in sentences:
        embedding = model.encode(sentence)
        embeddings.append(embedding)
    return embeddings

def embed_question(question):
    embeddings = []
    for words in question.split():
        embedding = model.encode(words)
        embeddings.append(embedding)
    return embeddings