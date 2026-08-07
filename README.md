# PrivaCPoliC

PrivaCPoliC is a Privacy Policy Summarizer and Question Answering application built using Natural Language Processing (NLP) and Retrieval-Augmented Generation (RAG).

The application allows users to upload a Privacy Policy PDF, generates a summary containing the important information from the document, and lets users ask questions about the uploaded policy through an interactive chat interface.

The goal of this project is to make long and complex privacy policies easier to understand by combining NLP techniques with semantic retrieval and Large Language Models (LLMs).

---

# Features

- Upload Privacy Policy PDF files
- Extract text from PDF documents
- Preprocess text using NLP techniques
- Generate embeddings and create a FAISS vector index
- Generate a summary of the uploaded Privacy Policy
- Ask questions about the uploaded document using RAG
- Continue asking follow-up questions without uploading the document again

---

# Technologies Used

### Backend

- Python
- Flask

### Frontend

- HTML
- CSS
- JavaScript

### Database

- SQLAlchemy

### NLP

- NLTK
- spaCy
- PyTextRank

### Embeddings

- Sentence Transformers

### Vector Database

- FAISS

### PDF Processing

- PyMuPDF
- BeautifulSoup

---

# Workflow 1 – Privacy Policy Summarization

### Step 1 – Upload PDF

The user uploads a Privacy Policy PDF to the application.

**Libraries Used**

- PyMuPDF
- BeautifulSoup

---

### Step 2 – Extract and Preprocess Text

The application extracts the text from the uploaded PDF and preprocesses it before further processing.

The preprocessing includes:

- Text cleaning
- Tokenization
- Stop-word removal
- Lemmatization

**Libraries Used**

- NLTK
- spaCy
- BeautifulSoup

---

### Step 3 – Chunking and Embedding

The processed text is divided into smaller chunks. Each chunk is converted into embeddings and stored in a FAISS vector index.

The processing includes:

- Propositional Chunking
- Embedding Generation
- Vector Index Creation

**Libraries Used**

- Sentence Transformers
- FAISS
- NumPy

---

### Step 4 – Summary Generation

The processed document is provided to the Large Language Model to generate a concise summary of the Privacy Policy.

**Libraries Used**

- Large Language Model (LLM)
- spaCy
- PyTextRank

---

# Workflow 2 – Question Answering using RAG

### Step 1 – Open Chat

After viewing the generated summary, the user can move to the chat page.

---

### Step 2 – Ask a Question

The user enters a question related to the uploaded Privacy Policy.

---

### Step 3 – Retrieve Relevant Information

The question is converted into an embedding and compared with the stored document embeddings using FAISS.

The application retrieves the most relevant chunks from the Privacy Policy.

The retrieval process includes:

- Query Embedding
- Similarity Search
- Top-K Chunk Retrieval

---

### Step 4 – Generate Answer

The retrieved chunks are added to the prompt and passed to the Large Language Model.

The model generates an answer based only on the retrieved context.

---

### Step 5 – Continue the Conversation

The user can continue asking follow-up questions or ask different questions about the uploaded Privacy Policy.

---

# Project Structure

```text
PrivaCPoliC/

│── app.py
│── config.py
│── requirements.txt
│── README.md
│
├── routes/
├── services/
├── database/
├── templates/
├── static/
├── uploads/
└── vector_store/
```

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
```

Move to the project directory.

```bash
cd PrivaCPoliC
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python app.py
```

Open the browser and go to:

```
http://127.0.0.1:5000/
```

---

# Future Improvements

- User authentication
- Chat history
- Support for multiple documents
- Export generated summaries
- Improve prompt engineering

---

# Project Status

PrivaCPoliC is currently a prototype. The core workflows for privacy policy summarization and Retrieval-Augmented Generation are implemented, and additional features will be added in future versions.

---

# License

This project is developed for educational purposes.