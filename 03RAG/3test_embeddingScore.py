
'''
In this program - we need to create embedding score to check similarity to compare 2 text
- 
'''
from openai import OpenAI
from similarity import cosine_similarity

# Create AI client
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

text1= "python is a programming language."
# text2= "Python is used for software develpment."
# text2 = "My name is rahul"
text2 = "Java is a programming language "


embedding1 = client.embeddings.create(
    model = "nomic-embed-text",
    input= text1
).data[0].embedding

embedding2 = client.embeddings.create(
    model = "nomic-embed-text",
    input= text2
).data[0].embedding


#Returns vector list
# # print(embedding1) 
print(len(embedding1)) #returns -768
print(len(embedding2)) #returns -768

score = cosine_similarity(embedding1, embedding2)
print("Embedding Score : ",score)