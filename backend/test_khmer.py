from gtts import gTTS

text = "សួស្តី ខ្ញុំឈ្មោះ ប្រូ កាក​​ ហា​ ហា ហា"

tts = gTTS(
    text=text,
    lang="km"
)

tts.save("khmer_test.mp3")

print("Khmer MP3 created successfully!")