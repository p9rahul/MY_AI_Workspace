# from retriver import load_docks

# documents = load_docks()

# for name, text in documents.items():
    
#     print(name)
#     print(text)
    
#     print("-"*40)

from retriver import retrive

filename, content =retrive("Tokio Marine Kiln")
print(filename)
print()
print(content)