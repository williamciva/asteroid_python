import speech_recognition as sr
import pyttsx3
import threading
import time

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def recognize():
    with sr.Microphone() as fonte:
        audio = recognizer.listen(fonte, timeout=0, phrase_time_limit=15)
    
    try:
        return recognizer.recognize_google(audio, language="pt-BR")
    except sr.UnknownValueError:
        speak("Não foi possível entender o áudio")
    except sr.RequestError as e:
        speak(f"Erro na requisição: {e}")


def restart_engine():
    global engine
    engine.stop()
    engine = pyttsx3.Engine()
        

def speak(*texts, is_async = False):
    def speak_blocking():
        text = " ".join(texts)
        engine.say(text)
        
        if engine._inLoop:
            engine.endLoop()

        engine.runAndWait()
        
    if is_async:
        return threading.Thread(target=speak_blocking, daemon=True).start()

    speak_blocking()