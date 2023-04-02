# Raspberry PI Chat GPT Voice Assistant ![alt text](https://raw.githubusercontent.com/iiiypuk/rpi-icon/master/128.png) 

Chat GPT Voice Assistant is an easy way to have chat GPT at home with the Raspberry PI.

## What do you need ?

Just a Raspberry PI, a microphone and speakers.

## How to install it

First you have to add the file chatgpt.py to your raspberry pi.

Before launching the script you need to install the following modules :

````
pip install openai
pip install SpeechRecognition
````

In the chatgpt.py file, you will have replace the ai_name by what you want. It's important to choose a distinguished name
because you will have to say it every time you talk to him.

Then you will have to assign the openai.api_key, you can get an api key from here https://platform.openai.com/ : just create an account and get an api KEY. 

You can change the model engine if you want.

Finally execute the script :

````
python chatgpt.py
````

You should hear a "Hello, I am <Bot name>" and you can ask questions to your new chat GPT assistant. Don't forget to say the AI's name every time you talk to him.

## Execute the script on Raspberry PI startup

If you don't want to execute the script manually, you can choose to execute the script on your Raspberry PI startup.

The method used here is to use systemd services.

Copy the chatgpt.service file from this repo to the following path :

````
/lib/systemd/system/
````

Next :

````
sudo systemctl daemon-reload
sudo systemctl enable chatgpt.service
````

Finally reboot to test if it works :

````
sudo reboot
````