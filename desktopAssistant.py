import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser #to open websites
import os

# for choosing voice type(male/female) and other setup
engine = pyttsx3.init('sapi5')
# sapi is speech API ,Helps in synthesis and recognition of voice

voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)
# engine.setProperty('volume', 1)
# engine.setProperty('rate', 10)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    print("I am MUSA Sir. Please tell me how may I help you") 
    speak("I am MUSA karim Sir. Please tell me how may I help you") 


def takeCommand():
    #It takes microphone input from the user 
    # and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")     
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        speak("Say that again please...")
        return "None" #None string will be returned
    return query

 
if __name__=="__main__" :
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case
        # print(query)
        # Logic for executing tasks based on query
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open chrome' in query:
            # webbrowser.open("google.com")
            os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'quit' in query:
            speak('Are You Sure ,Sir')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('God Bless You!')
                exit()
        elif 'play song' in query:
            music_dir = "C:\\Users\\mozam\\Desktop\\videos"
            songs = os.listdir(music_dir)
            from random import randint
            active=randint(0,len(songs)-1)
            print('playing',songs[active])    
            os.startfile(os.path.join(music_dir, songs[active]))
 