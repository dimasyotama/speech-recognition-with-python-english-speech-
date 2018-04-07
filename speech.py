import speech_recognition as sr
 
# Rekam Audio
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Bicaralah"+" Ngomong Inggris lu Harus !!!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    print("Hasil Ngomong: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Lau lu sokap kagak ngomong bahasa inggris")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
