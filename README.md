🏥 Medical AI Chatbot
An intelligent Medical Information Retrieval system built using Llama-2, LangChain, and Pinecone/FAISS. This bot allows users to query medical knowledge bases and receive context-aware responses based on uploaded medical PDF documents.

🚀 Overview
This project implements a RAG (Retrieval-Augmented Generation) pipeline. Instead of relying solely on a pre-trained model's static knowledge, this bot "reads" medical textbooks or documents to provide accurate, cited answers to user queries.

🛠️ Tech Stack
LLM: Llama-2-7B-Chat (GGML version)

Framework: LangChain

Vector Database: FAISS / Pinecone

Embeddings: HuggingFace Instruction Embeddings (sentence-transformers)

Frontend: Chainlit (for the chat interface)

Language: Python 3.9+

📂 Project Structure
Plaintext
├── data/              # Store your medical PDF documents here
├── vectorstore/       # Local FAISS index storage
├── model/             # Pre-trained LLM weights (e.g., llama-2-7b-chat.ggmlv3.q4_0.bin)
├── ingest.py          # Script to process PDFs and create vector embeddings
├── model.py           # Core logic for the LLM and Chainlit integration
├── requirements.txt   # Project dependencies
└── setup.py           # Environment setup
⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/ritesh2687/medical_bot.git
cd medical_bot
2. Create a Virtual Environment
Bash
python -m venv mbot_env
source mbot_env/bin/activate  # On Windows: mbot_env\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Download the Model
Download the Llama-2-7B-Chat GGML model (or any compatible .bin file) from HuggingFace and place it in the model/ directory.

5. Ingest Data
Place your medical PDF files in the data/ folder, then run:

Bash
python ingest.py
This will chunk the text, generate embeddings, and save them into the vectorstore/.

💻 Usage
Run the chatbot interface using Chainlit:

Bash
chainlit run model.py -w
Navigate to http://localhost:8000 in your browser to start chatting with your medical assistant.

🧠 How It Works
Data Ingestion: ingest.py extracts text from PDFs and splits it into manageable chunks.

Vectorization: Each chunk is converted into a vector embedding using HuggingFace models.

Semantic Search: When a user asks a question, the system searches the vector database for the most relevant document chunks.

Augmented Generation: The retrieved chunks + the user question are sent to Llama-2 to generate a human-like, accurate response.

⚠️ Disclaimer
This chatbot is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a physician or other qualified health provider with any questions you may have regarding a medical condition.
