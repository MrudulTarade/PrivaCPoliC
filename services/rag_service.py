import nltk
from embedding_service import embedded_sentences
from vectorization import create_index, save_index

def generate_answer(question):
    question = question.lower()
    embedded_question = embedded_sentences([question])[0]
    vector_index = create_index(embedded_question)
    save_index(vector_index, f"vector_store/question_vector/{question}.index")
    return "Answer generated for the question: " + question