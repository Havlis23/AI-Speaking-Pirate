from tkinter import *

from openai import OpenAI
import requests
import pygame

client = OpenAI(api_key='your-api-key-here')

root = Tk()
root.geometry("800x300")
root.title("AI Chatbot")

ai_response = StringVar()
status_message = StringVar()

def generate_content():
    status_message.set("Generating...")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jsi pirát a odpovídáš jako pirát, říkáš hodně vtipů a snažíš se být co nejvíce vtipný. Dávej si pozor na skloňování v češkém jazyce. "},
            {"role": "user", "content": user_input.get()}
        ],
        max_tokens=200  # The maximum number of tokens to generate in the completion
    )
    print("clovek: ", user_input.get())
    content = completion.choices[0].message.content
    print("AI: ", content)
    transcribe_to_speech(content)
    ai_response.set(content)
    status_message.set("Done")




def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def transcribe_to_speech(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/D38z5RcWu1voky8WS1ja"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "your-api-key-here"
    }
    data = {
        "text": text,  # Use the content as the value for the "text" field
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open('output.mp3', 'wb') as f:
            f.write(response.content)
        print("MP3 file has been saved as 'output.mp3'")
        play_audio('output.mp3')
    else:
        print(f"API request failed with status code {response.status_code}")

# Create a StringVar to hold user input
user_input = StringVar()

# Create a label and entry field for user input
(Label(root, text="Enter your text:",
      bg = "white",
       fg = "black",)
 .pack(pady=50))
Entry(root, textvariable=user_input,
      bg="white",
      fg="black").pack()

Label(root, textvariable=status_message, bg="white", fg="black").pack()


Label(root, textvariable=ai_response, bg="white", fg="black").pack()


# Create a button to generate content
Button(root, text="Generate", command=generate_content).pack()

# Start the main loop
root.mainloop()
