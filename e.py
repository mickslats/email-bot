import speech_recognition as sr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
import pyttsx3

def takeCommand():
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'Bot heard {query}')
    except Exception as e:
        print("Say that again please") 
        return None 
    return query 

engine = pyttsx3.init('espeak')

def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 160)
    engine.setProperty('voice', voices[14].id)
    engine.say(audio)
    engine.runAndWait()



def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('#Your Email', '#Email Password')
    email = EmailMessage()
    email['From'] = '#your email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_dictionairy = {
    'name1': 'name1@gmail.com',
    'name2': 'name2@gmail.com',
    'name3': 'name3@hotmail.co.uk',
    'name4': 'name4@gmail.com',
    'name5': 'name5@yahoo.co.uk',
    # add more here if you wish 
    }

def get_email_info():
    speak("email to who")
    name = takeCommand()
    receiver = email_dictionairy[name]
    print(receiver)
    speak("What is the subject of your email?")
    subject = takeCommand()
    speak("What should i say in the email")
    message = takeCommand()
    send_email(receiver, subject, message)
    speak("Email sent")
    speak("Do you want me to send any more emails")
    send_more = takeCommand()
    if 'yes' in send_more:
        get_email_info()

