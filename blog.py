import os
import openai
import os 
from dotenv import load_dotenv
load_dotenv()


API_KEY=openai.api_key = os.getenv("API_KEY")

def generate_blog(paragraph_topic):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="'Write a paragraph about the following topic. ' + paragraph_topic",
    temperature=0.9,
    max_tokens=400,
    
    
  
    )

    retrieve_blog=response.choices[0].text
    return retrieve_blog
print(generate_blog('what is your day?'))