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

10. 


===========================================
1) Multiline comments? Ctrl +/  
- """ ... """ or ''' ... '''
- is called a triple-quoted string
- this is not technically a comment called comment-like block

2) Ask Dynamic Questions with Memory from LLM?
- We can create a memory for our chatbot.
- This memory is created by us using Python, not by the LLM.
- We can create an empty Python list and keep adding information to the list whenever needed.
3) use case - Integrate python tool manager with AI assistant - Use tools?
Example: Getting the current date/time, generating random numbers, or creating passwords.
- An LLM does not always know the current system date and time.
- So, we can write a Python program to get the current date and time.
- Our chatbot can use Python program for these tasks.
- The result from Python is then given to the chatbot/LLM.
- Python → Performs specific tasks/tools
- LLM (Ollama) → Answers general questions
4) Read files like txt, pdf?
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
5) What if the document has 500 pages?
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

