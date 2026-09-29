from openai import OpenAI
from dotenv import load_dotenv
import os
from retriver import load_docks
from embedding import create_embedding
from similarity import cosine_similarity

#Load Documents
documents = load_docks()

#create Empty Dictionary 
document_embeddings ={}

#Create a for loop to iterate all documents items
for filename, content in documents.items():
    document_embeddings[filename] = create_embedding(content)
    

#Load Congiguration like env file
load_dotenv()

#create a client that comminucate with ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" *40)
print("     Rahul 1stAI Assistant")
print("=" *40)

while True:

    user_input = input("\nYou : ")
    
    if user_input.lower() == "quit":
        print("\nAI : Goodbye! Have a great day.")
        break
    
    #Create Question Embedding asked by user
    question_embedding = create_embedding(user_input)
    
    #create global variable for score
    best_score= -1
    best_document =None
    
    for filename, embedding in document_embeddings.items():
        
        #cosine_similarity pass vectors
        score = cosine_similarity(question_embedding,embedding)
        
        #compare score and set best score
        if score > best_score:
            best_score = score
            best_document = filename
    #end of for loop
    
    #create Context variable and set best retrival document
    context = documents[best_document]    
    
    prompt =f"""
    Answer the question using only the following information.
    
    Context:{context}
    
    Question: {user_input}
    """
    #Create response
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
     
    print("\n AI Bot :", response.choices[0].message.content)
    print("Score : ",best_score)
    
