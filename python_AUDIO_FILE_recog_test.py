print("speech recog.py hello world!")
import speech_recognition as sr
print(sr.__version__)

recog = sr.Recognizer()
# recog.recognize_google()

fitness = sr.AudioFile("fittness.wav")
with fitness as source:
    recog.adjust_for_ambient_noise(source)
    audio = recog.record(source)
    print(type(audio))

    possibilities = recog.recognize_google(audio, show_all=True)
    
    # print all possibilities on their own line
    for possibility in possibilities["alternative"]:
        print(possibility["transcript"])
        