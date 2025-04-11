# pip install python-docx
# pip install unstructured
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from llm import QdrantVecStoreFromDocs
import nltk

def load_doc():
    #nltk.download('punkt_tab')
    #nltk.download('averaged_perceptron_tagger')

    word=UnstructuredWordDocumentLoader('D:\\workspace\\python\\Geek02\\class26\\数据字典.docx')
    docs=word.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=50,
                                              chunk_overlap=20)
    s_docs=splitter.split_documents(docs)
    QdrantVecStoreFromDocs(s_docs,"data")

if __name__ == '__main__':
    load_doc()