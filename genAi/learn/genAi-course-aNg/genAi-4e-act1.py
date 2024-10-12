print("Hello, World")
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def llm_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
	messages=[{'role':'user', 'content':prompt}],
	temperature=0
    )
    return response.choices[0].message['content']

prompt = '''
	Classify the following review as having either a positive or negative sentiment: 

	The banana pudding was really tasty!
'''

response = llm_response(prompt)
