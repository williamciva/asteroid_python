import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
recognizer = sr.Recognizer()

def recognize():
    with sr.Microphone() as fonte:
        audio = recognizer.listen(fonte, timeout=0, phrase_time_limit=15)
    
    try:
        return recognizer.recognize_google(audio, language="pt-BR")
    except sr.UnknownValueError:
        engine.say("Não foi possível entender o áudio")
    except sr.RequestError as e:
        engine.say(f"Erro na requisição: {e}")

def speak(*texts):
    f_text = ""
    for text in texts:
        f_text = f_text + " " + text
        
    engine.say(f_text)