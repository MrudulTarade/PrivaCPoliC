from flask import request, render_template, Blueprint, session
from services.rag_service import generate_answer

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def answer_question():
    question = request.form.get("question")
    #document_id = session.get("document_id")
    generated_answer = generate_answer(question)
    return render_template("chat.html",answer=generated_answer)
    