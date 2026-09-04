import re, faiss
import numpy as np
from werkzeug.utils import secure_filename
from sentence_transformers import SentenceTransformer
from services.embedding_service import embed_question
from services.vectorization import create_index, save_index, load_index, search

def generate_answer(question, file):
    file = secure_filename(file.filename)
    question = question.lower()
    question = re.sub(r'[^a-zA-Z0-9\s]', '', question)
    embedded_question = embed_question(question)
    vector_index = create_index(embedded_question)
    save_index(vector_index, f"vector_store/question_vector/{question}.index")
    index = load_index(f"vector_store/{file}.index")
    return "Answer generated for the question: " + question