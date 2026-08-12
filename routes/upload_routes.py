import pickle
from fileinput import filename
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from services.pdf_reader import extract_text
from services.preprocessing import clean_text, advanced_preprocessing
from services.chunk_service import extract_propositions
from services.embedding_service import embed_sentences
from services.vectorization import create_index, save_index
from services.summary_service import generate_summary

upload_bp = Blueprint("upload",__name__)

@upload_bp.route("/upload", methods=["GET"])
def upload_page():
    return render_template("upload.html")

@upload_bp.route('/upload', methods=["POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files["pdf_file" ]
        if file:
            filename = secure_filename(file.filename)
            file.save(f"uploads/{filename}")
            text = extract_text(f"uploads/{filename}")
            cleaned_text = clean_text(text)
            processed_text = advanced_preprocessing(cleaned_text)
            propositions = extract_propositions(cleaned_text)
            with open(f"vector_store/{filename}.pkl", "wb") as f:
                    pickle.dump(propositions, f)
            embeddings = embed_sentences(propositions)
            vector_index = create_index(embeddings)
            save_index(vector_index, f"vector_store/{filename}.index")
            summary = generate_summary(cleaned_text)
            session["summary"] = summary
        return redirect(url_for("summary.summary_page"))
    return render_template("upload.html", summary=summary)

