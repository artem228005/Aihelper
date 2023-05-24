import os
try:
	import openai
except Exception:
	os.system("pip install openai")

messages = []

def token(qq1):
	openai.api_key = qq1

def message(mes):
	global chat_response

	try:
		content = mes
		messages.append({"role": "user", "content": content})
		completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=messages)
		chat_response = completion.choices[0].message.content
		
	except Exception as e:
		print("e")