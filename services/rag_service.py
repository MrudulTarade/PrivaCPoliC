import re, faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from services.embedding_service import embed_question
from services.vectorization import create_index, save_index

def generate_answer(question):
    question = question.lower()
    question = re.sub(r'[^a-zA-Z0-9\s]', '', question)
    embedded_question = embed_question(question)
    vector_index = create_index(embedded_question)
    save_index(vector_index, f"vector_store/question_vector/{question}.index")
    return "Answer generated for the question: " + question