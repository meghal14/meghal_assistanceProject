import speech_recognition as sr
import pyttsx3
import webbrowser
import os

engine = pyttsx3.init()
# text = str(input("Enter text : "))
def say(text):
    engine.say(text)
    engine.runAndWait()

def takecommond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said : {query}")
            return query
        except Exception as e:
            return "Some error occure sorry from meghal's assistance"

if __name__=='__main__':
    say("Hello I am Meghal's Assistance")
    while True:
        print("Listning...")
        query = takecommond()
        say(query)

        #todo:add new site name and site address
        sites=[["youtube","https://www.youtube.com"],["google","https://www.google.com"],["Wikipedia","https://www.wikipedia.com"]]
        for site in sites:
            if f"open {site[0]}" in query.lower() :
                say(f"opening {site[0]}")
                webbrowser.open(site[1])

        #todo:add new music paths
        if "open music" in query.lower() or "play music" in query.lower():
            music_path = r"C:\Users\Admin\Downloads\doodoobaabaa.co.za - With You - AP Dhillon (Official Music Video) (320 KBps).mp3"
            os.startfile(music_path)

        if f"open word" in query.lower():
            say("Opening word")
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")

        if f"open calculator" in query.lower():
            say("Opening Calculator")
            os.system("calc.exe")

        if f"open chat gpt" in query.lower():
            say("opening chatgpt")
            webbrowser.open("https://chatgpt.com")
