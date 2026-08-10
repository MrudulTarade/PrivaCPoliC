from flask import Blueprint, render_template, url_for, redirect, request, session

summary_bp = Blueprint("summary",__name__)

@summary_bp.route("/summary", methods=["GET"])
def summary_page():
    return render_template("summary.html")

@summary_bp.route("/summary", methods=["POST"])
def chat_page():
    if request.method == 'POST':
        return redirect(url_for("summary.chat_page"))
    return render_template("summary.html")