import nltk, spacy, pytextrank

def generate_summary(text):
    nlp = spacy.load("en_core_web_sm")
    nlp.pipeline.add("textrank")
    doc = nlp(text)
    for sent in doc._.textrank.summary(limit_phrases=15, limit_sentences=5):
        return sent.text
    
