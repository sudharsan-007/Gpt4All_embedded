import ollama

# mistral, llama2-uncensored
response = ollama.chat(model='mistral', messages=[
  {
    'role': 'user', # "system", "user" , "assistant"
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content']) 
