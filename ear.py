import speech_recognition as sr

recognizer = sr.Recognizer()

def heart():

    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        print('say something ......')
        audio = recognizer.listen(mic,phrase_time_limit=3)
    try:
        voice = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        voice = 'bla bla'

    return voice