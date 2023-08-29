#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pyttsx3


# In[ ]:


pipwin install pyaudio


# In[ ]:


pip install SpeechRecognition


# In[ ]:


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser


# To install PyAudio  : https://www.lfd.uci.edu/~gohlke/pythonlibs/

# In[ ]:


engine  = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


# In[ ]:


#print(voices[0].id)


# In[ ]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("It is a fine morning sir !")
    elif hour>=12 and hour<18:
        speak("Hope you had your lunch, Good afternoon sir !")
    else:
        speak("The weather is lovely, Good evening")
        
    speak("Hello how are you? I am your personel assistant chitti! how can i help you")


# In[ ]:


greet()


# In[ ]:


def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1.2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("I could not get you, please speak again")
        return "None"
    return query


# In[ ]:


if __name__ == "__main__":
    greet()
    while True:
        if 1:
            query = command().lower()
            
            if 'wikipedia' in query:
                speak('Searching Wikipedia')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(f'{query}',sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open instagram' in query:
                webbrowser.open("instagram.com")
            elif 'open youtube' in query:
                webbrowser.open("Youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open kaggle' in query:
                webbrowser.open("kaggle.com")
            elif 'the weather' in query:
                webbrowser.open("weather.com")
            elif 'the score' in query:
                webbrowser.open("cricbuzz.com")
            elif 'play music' in query:
                music_dir = 'Urban Sound\\fold2'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                
            
                
            
                


# In[ ]:




