from flask import Blueprint, render_template

summary_bp = Blueprint("summary",__name__)

@summary_bp.route("/summary", methods=["GET"])
def summary_page():
    return render_template("summary.html")

@summary_bp.route("/chat", methods=["GET", "POST"])
def chat_page():
    return render_template("chat.html")