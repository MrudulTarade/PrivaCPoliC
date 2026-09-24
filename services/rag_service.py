import re, faiss, pickle
import numpy as np
from werkzeug.utils import secure_filename
from sentence_transformers import SentenceTransformer
from services.embedding_service import embed_question
from services.vectorization import create_index, save_index, load_index, search
from services.prompt_service import create_answer

def generate_answer(question, file):
    file = secure_filename(file.filename)
    question = question.lower()
    question = re.sub(r'[^a-zA-Z0-9\s]', '', question)
    embedded_question = embed_question(question)
    vector_index = create_index(embedded_question)
    save_index(vector_index, f"vector_store/question_vector/{question}.index")
    index = load_index(f"vector_store/{file}.index")
    indices = index.search(embedded_question, 3)
    with open(f"vector_store/{file}.pkl", "rb") as f:
        propositions = pickle.load(f)
    related_chunks = []
    for i in indices:
        if indices[i] == propositions[i]:
            related_chunks.append(propositions[i])
    context = " ".join(related_chunks)
    answer = create_answer(question, context)

