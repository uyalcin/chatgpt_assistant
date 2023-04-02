import openai
import os
import speech_recognition as sr
import time

ai_name = "name"
model_engine = "gpt-3.5-turbo"
openai.api_key = ""
start_message = "\"Hello, I am " + ai_name + "\""

r = sr.Recognizer()

def GPT(query):
   completion = openai.ChatCompletion.create(
    model=model_engine,
    messages=[
    {"role": "user", "content": query}
  ]
)
   return completion.choices[0].message.content

os.system("espeak " + start_message)
try:
    while True:
       with sr.Microphone() as source:
           audio = r.listen(source)
           try:
               words = r.recognize_google(audio)
           except:
               words = "silence"
           print(words)
       if ai_name in words.lower():
           res = GPT(words)
           cmd = "espeak \"\"\"" + str(res) + "\"\"\""
           print(cmd)
           os.system(cmd)
except KeyboardInterrupt:
    print("\nExiting ChatGPT")
