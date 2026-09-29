from pathlib import Path

# use for to load documents
def load_docks():
    # Create a dictionary
    documents = {}
    
    folder =Path("data")
    
    for file in folder.glob("*.txt"):
        documents[file.name]= file.read_text(encoding="utf-8")
        
    return documents
'''
-Function to retrive exact match if question exist then return filename & content 
 if 2 match then return 1st one
-
'''
def retrive(question):
    
    documents = load_docks()
    question = question.lower()
    for filename, content in documents.items():
        if question in content.lower():
            return filename, content
    return None, None