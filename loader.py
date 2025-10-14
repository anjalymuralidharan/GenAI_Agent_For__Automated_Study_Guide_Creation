"""
Data loader pages 
1. loads pdf data
2. split data into chunks
3. Stored in a vector database
"""

import os
from langchain_community.document_loaders import PyPDFLoader
import pprint
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from uuid import uuid4



def LoadData():
    filename = input("Enter your filename (with or without .pdf extension): ")
    if not filename.endswith('.pdf'):
        filename += '.pdf'
    file_path = f"input/{filename}"
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found!")
        print("Available files in sample directory:")
        if os.path.exists("sample"):
            for file in os.listdir("sample"):
                if file.endswith('.pdf'):
                    print(f"  - {file}")
        return None
    try:
        print(f"📄 Loading PDF: {file_path}")
        loader = PyPDFLoader(file_path)
        docs = loader.load()   
        aggregated_content = ""
        file_ = ""
        for i, doc in enumerate(docs):
            aggregated_content += doc.page_content
            file_ += f"\n{doc.page_content}"
        WritetoFile("loaded" , file_)
        print(f"📦 Aggregated all {len(docs)} pages into single content string")
        return (aggregated_content,filename.split(".")[0])
       
    except Exception as e:
        print(f"❌ Error loading PDF:{e}")
        return None
def WritetoFile(file_path ,docs ):
    """
    this is a test function writtern to verify
    """
    try:
        with open('loaded.txt', 'w', encoding='utf-8') as f:
            f.write(docs)
            
        print(f"💾 All data has been written to 'loaded.txt'")
        
    except Exception as write_error:
        print(f"❌ Error writing to loaded.txt: {write_error}")
def CreateChunks(content):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
    )
    texts = text_splitter.create_documents([content])
    return texts
    

    
    
    
