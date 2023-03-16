
print("tts_text.py hello world!")

from gtts import gTTS
import os
my_Text = "Hello World! this is some text!"
my_Language = "en"

audio = gTTS(text=my_Text, lang=my_Language, slow=True)
audio.save("example.mp3")
os.system("start example.mp3")

