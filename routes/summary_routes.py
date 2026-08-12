from flask import Blueprint, render_template, session

summary_bp = Blueprint("summary",__name__)

@summary_bp.route("/summary", methods=["GET"])
def summary_page():
    summary = session.get("summary")
    return render_template("summary.html", summary=summary)

@summary_bp.route("/chat")
def chat_page():
    
    return render_template("chat.html")