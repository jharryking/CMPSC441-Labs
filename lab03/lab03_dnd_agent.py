from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

sign_your_name = 'Harry King'
model = 'gemma3:270m'
options = {'temperature': 0.60, 'max_tokens': 100}
messages = [
  {'role': 'system', 'content': (
    'You are an assistant that has human emotions. '
    'Respond naturally, and after answer ask a relevant '
    'question and/or comment to continue the conversation. '                        
    'Only use letters, numbers, and basic punctuation in responses. '
    'Kindly greet the user to open the conversation. '
    )},
]


# But before here.
messages.append({'role':'user', 'content':''}) # An empty user message to prompt the model to start responding.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  #Get the agents's response
  response = chat(model=model, messages=messages, stream=False, options=options)
  messages.append({'role': 'assistant', 'content': response.message.content})
  print(f'Agent: {response.message.content}')


  #Get the user's prompt
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

