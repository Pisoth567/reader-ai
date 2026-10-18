from gtts import gTTS

text = "Hello, my name is Net Pisoth. I am a Computer Science student."

tts = gTTS(
    text=text,
    lang="en"
)

tts.save("english_test.mp3")

print("English MP3 created successfully!")