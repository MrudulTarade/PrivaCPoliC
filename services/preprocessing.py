import nltk, re, string
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from services.pdf_reader import extract_text


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

#Clean the text
def clean_text(pdf_path):
    text = extract_text(pdf_path)
    text = text.lower()
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

cleaned_corpus = clean_text('path/to/your/pdf/file.pdf')

#Tokenize the cleaned text
tokenized_corpus = word_tokenize(cleaned_corpus)

#Remove stop words
stop_words = set(stopwords.words('english'))
filtered_corpus = [word for word in tokenized_corpus if word not in stop_words]

#Lemmatize the filtered text
lemmatizer = WordNetLemmatizer()
lemmatized_corpus = [lemmatizer.lemmatize(word) for word in filtered_corpus]

