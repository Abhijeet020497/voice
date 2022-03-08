from tkinter import Message
import pyttsx3 # text to speech
import datetime
import speech_recognition as sr #speech recognition
import smtplib
from secrets import senderemail, epwd, to 
from email.message import EmailMessage
import pyautogui
import webbrowser as web
from time import sleep
import subprocess
import wikipedia
import pywhatkit

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice==1:
        engine.setProperty('voice',voices[0].id)
        speak('hello this is VIV')
    
    if voice==2:
        engine.setProperty('voice',voices[1].id)
        speak('hello this is VIV')
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak('Current time is ')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('Current date is ')
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back")
    greeting()
    time()
    date()
    speak("VIV online, how can i help you")

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommandCMD():
    query = input("how can i help you?")
    return query

def takeCommandMic():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again..,")
        return "None"
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendWhatsAppmsg(phone_no, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text'+Message)
    sleep(10)
    pyautogui.press('enter')

def searchGoogle():
    speak('What should I search for?')
    search = takeCommandMic()
    web.open('https://google.co.in/search?q='+search)

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommandMic().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'exit' in query:
            exit()
        elif 'email' in query:
            email_list = {
                'test email':'abhijeetshetty1997@gmail.com'
            }
            try:
                speak('to whom you want to send mail?')
                name = takeCommandMic()
                receiver = email_list[name]
                speak('what is the subject of the mail?')
                subject = takeCommandMic()
                speak('What should I say?')
                content = takeCommandMic()
                sendEmail(receiver,subject,content)
                speak('Email has been send')
            except Exception as e:
                print(e)
                speak('Unable to send the email')

        elif 'message' in query:
            user_name = {
                'viv': '+918452896807'
            }
            try:
                speak('to whom you want to send the WhatsApp msg?')
                name = takeCommandMic()
                phone_no = user_name[name]
                speak('what is the message?')
                message = takeCommandMic()
                sendWhatsAppmsg(phone_no,message)
                speak('Message has been send')
            except Exception as e:
                print(e)
                speak('Unable to send the message')

        elif 'wikipedia' in query:
            speak('searching on wikipedia.... ')
            query = query.replace('wikipedia')
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
     
        elif 'search' in query:
            searchGoogle()
            
        elif 'youtube' in query:
            speak('what should i search for on youtube')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)
            
        elif 'offline' in query:
            quit() 
        elif "sign out" in query:
            speak("Ok , your pc will log off in make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

