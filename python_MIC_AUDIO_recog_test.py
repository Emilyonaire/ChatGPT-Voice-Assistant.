print("speech recog.py hello world!")
import speech_recognition as sr, openai, os, subprocess
from gtts import gTTS
print(sr.__version__)

openai.api_key = "API-KEY"

wakeword = "WAKE"
killcode = "EXIT"
ended = False

# functions
def askQuestion(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

# listen for audio
def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        print("Got audio, transcribing...")
        try:
            text = r.recognize_google(audio)
            inputText = (text).upper()
            print("Done, transcribed as \"" + inputText + "\"")
            words = parseSentenceToArrayOfWords(inputText)
            return [words, inputText]
        except sr.exceptions.UnknownValueError as unknownError:
            print("Error, could not transcribe audio")
            return ["ignore", "ignore"]
        except openai.error.RateLimitError:
            print("Error, rate limit exceeded")
            return ["ignore", "Rate Limit Exceeded."]

# parse Sentence To Array Of Words
def parseSentenceToArrayOfWords(sentence):
    words = sentence.split(" ")
    return words

#inverse of above
def parseWordsToSentence(words):
    sentence = ""
    for word in words:
        sentence += word + " "
    print("sentence: " + sentence)
    return sentence

#say phrase
def sayPhrase(phrase):
    print(phrase)
    audio = gTTS(text=phrase, lang="en", slow=False)
    audio.save("response.mp3")
    audio_path = os.getcwd() + "\response.mp3"
    print(audio_path)
    
    speed = 1.5
    command = ["ffplay", "-nodisp", "-autoexit", "-af", "atempo={}".format(speed), audio_path]
    subprocess.call(command)


r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

    #Loop over recognized text and listen specifically for wake word/phrase
    #if wake word/phrase is heard, then start listening for commands
    #if wake word/phrase is not heard, then go back to listening for wake word/phrase
while(ended != True):
    Transcribed = listen()

    # if wake word/phrase is heard in list of words
    if(wakeword in Transcribed):
        print("Wake word heard, listening for commands...")
        words, reuters = listen()
        print("Done, transcribed as \"" + reuters + "\"")
        sayPhrase(askQuestion(reuters))

    #if heard killcode, then end the program
    elif(killcode in Transcribed):
        print("Killcode heard, ending program...")
        ended = True

    #if "ignore" is heard, then go back to listening for wake word/phrase
    elif("ignore" in Transcribed):
        print("Nothing heard, going back to listening for wake word/phrase...")

    else:
        print("Wake word not heard, going back to listening for wake word/phrase...")