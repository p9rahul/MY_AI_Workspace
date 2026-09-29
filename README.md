1. Download & Install python
2. Install VS code
3. Download & Install ollama https://ollama.com/download/windows
4. Download AI model
   $ollama pull qwen3:4b or 
	$ollama pull qwen3:1.7b
5. Verify ollama is working?
   $ollama run qwen3:4b
	$ollama run qwen3:1.7b

6. Create a project & Open in VS code
7. Create Virtual Env
   $python -m venv .rkenv 
	$.rkenv\Scripts\activate

8. Open project VS code terminal
   Install python library
   $pip install openai python-dotenv
9. Question - Create a small AI assistant?
   Create .env file inside 01Day folder
   add following lines-
   BASE_URL=http://localhost:11434/v1
   API_KEY=ollama
   MODEL=qwen3:1.7b

10. other LLM - Now Jev, openrouter

===========================================

1. Multiline comments? Ctrl +/

- """ ... """ or ''' ... '''
- is called a triple-quoted string
- this is not technically a comment called comment-like block

2. Ask Dynamic Questions with Memory from LLM?

- We can create a memory for our chatbot.
- This memory is created by us using Python, not by the LLM.
- We can create an empty Python list and keep adding information to the list whenever needed.

3. use case - Integrate python tool manager with AI assistant - Use tools?
   Example: Getting the current date/time, generating random numbers, or creating passwords.

- An LLM does not always know the current system date and time.
- So, we can write a Python program to get the current date and time.
- Our chatbot can use Python program for these tasks.
- The result from Python is then given to the chatbot/LLM.
- Python → Performs specific tasks/tools
- LLM (Ollama) → Answers general questions

4. Read files like txt, pdf?
   - in this chapter will read, how to read files
   - "use case" - Suppose we have a document containing our company or industry information.
   - This information may not be available in the LLM because:
     - LLMs are generally trained on public or available datasets.
     - They don't automatically know our private company documents.
     - We can provide our documents to the application.
     - The application can then use the document to answer our questions.
       Company Document
       ↓
       Our Chatbot
       ↓
       LLM
       ↓
       Answer based on our document
5. What if the document has 500 pages?

- Sending the entire 500-page document to the LLM every time is difficult and inefficient.
  Solution: RAG

500-page document
↓
Break document into smaller chunks
↓
Find the relevant chunk
↓
Send only the relevant information to LLM
↓
LLM generates the answer

So, instead of sending the entire document, RAG finds the relevant information and sends that information to the LLM.

6. RAG?

- Retrival Before generation, Generate after Retrival
- Embedding - goto 03RAG retriver.py and read
- NumPy (Numerical Python) is the fundamental open-source library for scientific computing, data science, and machine learning in Python $pip install numpy
-

'''
Problem - in above it match exact but we need similar search
#Embedding - it allow simentic similarity rather than exact word - our above retrival search exact word - But human searches for meaning - Embedding don't replace retrival but make smarter
#Use case -
Question1- What is an automobile?
Question2- What is a car?
Answer - as a human we know both are similar but computer doesn't know,it's a different words

#use case -
Our knowledge base means files contains- Python is a programming language.
Question - What is a coding language? - our computer search exact word but not meaning

# Delhi(latitude, longitude) if two cities are close on map, we say both are are geogrphically close

# Embedding work in a very similar way except instead of placing cities on a map , they place meanings in a

mathematical way.

- if 2 words have similar meaning they are similar or closer

#What is embedding search? - to search similar words

- it is list of number that represent the meaning of some text
  ex- python -> [.2,.3,-.5] -> this list called vector
  and programming language -> [.2,.3,-.51]

both looks similar, best match

Q) why convert words into number?

- Because computers best to understand numbers not text, every text converts into numbers

Q) Do we Create Embedding ourselves?

- No, as we don't build LLM models,we won't build embedding models
  -will use pre-trained embedding models
  -as AI devlopers just focus of using this not plot dimensions like 2D,3D,567D vectors

Similar search
Pizza - Burger
Car - Automobile
Home - Building
Rice - Database no

#Embedding model - nomic-embed-text for ollama

1. install this,open cmd $ollama pull nomic-embed-text
2. check 0 ollama list
   C:\Users\pc>ollama list

NAME ID SIZE MODIFIED
nomic-embed-text:latest 0a109f422b47 274 MB 3 seconds ago
qwen3:1.7b 8f68893c685c 1.4 GB 5 days ago

    - chat model - Writes answer, Understand conversation, generate text, used for Chatting
    - Embedding model - produce vectors, Represent meaning, Generates numbers, used for searching

API method-
we used for chat - client.chat.completions.create()
Embedding - client.chat.embedding.create()

**\*\*\*\*** Now, Cosine similarity **\*\*\*\***

- use for compare embedding & create score -for 2 string similiratiy
- Create score for "semantic search"
  ex - Question - what is london insurance company?
- search in all 4 docks and compare
  Document Score
  EyProject1.txt 90%
  EyProject2.txt 60%

- Embedding are only useful to compare to text/sentences/paragraph
- Cosine similarity use for to measure closeness based on Embedding score
- Higher similarity means more relevant
- Now, Retrival is no longer based on exact search --- it is based on meaning

**\*\*\*** Now, we will build a complete RAG system that**\*\*\***

1. loads documents
2. Create embedding

3. use AI model to answer questions from relevant documents

Solution -
User question -> Generate Question embedding -> Compare with all Documents ->Find Best match
-> Send only that documents to AI LLM -> Generate Final Answer & Display Answer

Important Notes- AI model never searches, python propram the search , AI answer using retrived
information. This makes RAG efficient.

Question? - Suppose you have 10K documents, Would you generate embeddings everytime when user ask question?
Answer - of Course not.

- That is waste of time
  instead, load documents once -> generate embedding ->Store them -> Reuse them -> only you need to create
  Embedding for "asked question"

Algorithm -

1. Load Documents
2. Create Embedding once for all 10K documents "Knowledge Base"
3. Create "Cosine Score" & Compate score with each new line -> if best score is high then store inside varible
4. Retrive Best documents & send it to LLM (Retrive the relevant information based on Score (Compare similarity for 2 text) )
5. Now Convert question into embedding
6. send both Retival file & Question

Now, your knlowledge base will be utilize for asked question

- like private data
- no need to train AI LLM model on your data

Knowledge Base -> Embedding -> Similarity search -> Retrive -> LLM -> Answer

# are we perfect?

- not yet
  For Example -
  Our search refer to only 1 documents
- What if answer is spread across 3 documents?
- In this way 1 documents retrive but still 200 pages
  answer - Professional RAG system solve this using chunking, persistent vector, top-n retrival,ranking,
  meta data filtering & Hybrid search
- Core workflow will remain same only few changes will require
- Here , we have learn How RAG works?
  '''
  Limitation - But in my docks 2 rahul in 2 docks but here RAG retrive from 1 document so 1 search.
  You : how many rahul are there and describe their roles

AI Bot : There is **one Rahul** in the context. His role is as a **Business Analyst (BA)**.
