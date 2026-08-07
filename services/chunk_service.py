import spacy


nlp = spacy.load("en_core_web_sm")

def extract_propositions(text):
    doc = nlp(text)
    propositions = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ in ("ROOT", "conj"):
                proposition = " ".join([token.text for token in token.subtree])
                propositions.append(proposition)
    return propositions