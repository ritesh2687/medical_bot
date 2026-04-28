from setuptools import find_packages,setup

setup(
    name='medical_bot',
    version='0.1.0',
    author='Ritesh Prajapati',
    description='A medical chatbot application',
    author_email='ritesh450718@gmail.com',
    packages=find_packages(),
    install_requires=[
        'langchain==0.3.26',
        'flask==3.1.1',
        'sentence-transformers==4.1.0',
        'pypdf==5.6.1',
        'python-dotenv==1.1.0',
        'langchain-pinecone==0.2.8',
        'langchain-community==0.3.26',
        'langchain-groq==0.3.8',
        'langchain-huggingface',
    ],
)