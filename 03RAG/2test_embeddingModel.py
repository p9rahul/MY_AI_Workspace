from openai import OpenAI

# Create AI client
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

text1= "python is a programming language."
text2= "Python is used for software develpment."

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