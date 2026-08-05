from fileinput import filename
from flask import *
from werkzeug.utils import secure_filename
from services.pdf_reader import extract_text
from services.preprocessing import clean_text, advanced_preprocessing
from services.chunk_service import split_sentences
from services.chunk_service import extract_propositions

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(filename)
            cleaned_text = clean_text(filename)
            processed_text = advanced_preprocessing(cleaned_text)
            sentences = split_sentences(processed_text)
            propositions = extract_propositions(cleaned_text)
            return redirect(url_for('display', filename=filename, sentences=sentences, propositions=propositions))
    return render_template('templates\\summary.html')

if __name__ == '__main__':
    app.run(debug=True)