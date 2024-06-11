from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 

app = Flask(__name__)

DATA_PATH = 'athdp/'
DB_FAISS_PATH = 'athvs/athdb'

# Ensure the upload directory exists
if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)

# Function to save uploaded file
def save_file(file):
    filename = secure_filename(file.filename)
    file_path = os.path.join(DATA_PATH, filename)
    file.save(file_path)
    return file_path

# Create vector database
def create_vector_db(file_path):
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        file_path = save_file(file)
        create_vector_db(file_path)
        return jsonify({"message": "File uploaded and processed successfully"}), 200

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

if __name__ == "__main__":
    app.run(debug=True, port=6000)
