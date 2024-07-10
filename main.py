import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai
import os
from gtts import gTTS
import pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize pygame
    pygame.init()

    # Specify the path to your MP3 file
    filename = "path/to/your/song.mp3"

    # Load the audio file
    pygame.mixer.music.load("temp.mp3")

    # Play the audio file
    pygame.mixer.music.play()

    # (Optional) Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.event.pump()

    # Quit pygame
    pygame.quit()


def aiprocess(command):
  def get_api_key():
    """
    Returns your Gemini API key (replace with your actual key).
    """

  try:
    genai.configure(api_key=get_api_key())
  except Exception as e:
    print(f"Error configuring API: {e}")
    exit(1)  # Exit the script with an error code

  model = genai.GenerativeModel('gemini-1.5-flash')

  response = model.generate_content(command)
  return response.text  # Print the generated content


def processCommand(c):
    if "open google" in c.lower():
        wb.open("https://google.com")
    elif "open youtube" in c.lower():
        wb.open("https://youtube.com")
    elif "open facebook" in c.lower():
        wb.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        wb.open(link)
    elif "news" in c.lower():
        if r.status_code == 200:
            # Processing the response data (json format)
            data = r.json()
            
            # Extracting headlines
            articles = data['articles']
            for article in articles:
                title = article['title']
                speak(title)

    else:
        # Let OpenAI handle the request
        output = aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word Jarvis
        # Capture audio input from the microphone                                                                             
        r = sr.Recognizer()                                                                                   
            
        print("recognizing...")
        try:
            with sr.Microphone() as source:                                                                       
                print("Listening...")                                                                                   
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:                                                                       
                    print("Jarvis Active...")                                                                                   
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
 
        except Exception as e:
            print("Error: {0}".format(e))


