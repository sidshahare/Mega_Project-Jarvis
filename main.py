import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai
from gtts import gTTS
import pygame
import os

# Ensure you have set your OpenAI API key as an environment variable
# export OPENAI_API_KEY="your_openai_api_key"

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "db27580d51274f368cea3a08195e6590"
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-PRRRp3noUQ1QMbA8dOIf_t5s75q9I3t2u8MBZi0TTUT3BlbkFJbpi7nYbayWx6Thw27da6rZJTmbDujzS1MTMVe6bjoA")

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def aiProcess(command):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message['content']

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ", 1)[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # Limit to first 5 headlines
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news.")
    else:
        output = aiProcess(command)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes?")
                    print("Jarvis Active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
