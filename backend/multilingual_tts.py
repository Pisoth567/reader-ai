from gtts import gTTS
from pydub import AudioSegment
from language_detector import detect_language

import os
import uuid


def generate_multilingual_audio(text):
    parts = detect_language(text)

    final_audio = AudioSegment.empty()

    for part in parts:

        language = part["language"]
        text_part = part["text"].strip()

        # Ignore empty parts
        if not text_part:
            continue

        print(f"Language: {language}")
        print(f"Text: {text_part}")

        # Temporary filename
        filename = f"temp_{uuid.uuid4()}.mp3"

        # Choose voice
        if language == "km":
            tts = gTTS(
                text=text_part,
                lang="km"
            )
        else:
            tts = gTTS(
                text=text_part,
                lang="en"
            )

        # Generate temporary MP3
        tts.save(filename)

        # Load MP3
        audio = AudioSegment.from_mp3(filename)

        # Add to final audio
        final_audio += audio

        # Delete temporary file
        os.remove(filename)

    # Save final audio
    output_file = "multilingual_result.mp3"

    final_audio.export(
        output_file,
        format="mp3"
    )

    return output_file


# Test
text = "Hello, my name is នេត ពិសុទ្ធ. I am a Computer Science student."

output = generate_multilingual_audio(text)

print()
print("================================")
print("Audio created successfully!")
print(f"File: {output}")
print("================================")