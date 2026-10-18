from gtts import gTTS
from pydub import AudioSegment

import os
import uuid
import re

from language_detector import detect_language


# Folder where generated MP3 files will be stored
AUDIO_DIR = "audio"

os.makedirs(AUDIO_DIR, exist_ok=True)


def generate_multilingual_audio(text: str):
    """
    Convert mixed English + Khmer text into one MP3 file.

    Example:
        Hello, my name is នេត ពិសុទ្ធ.

    Processing:
        English → English TTS
        Khmer   → Khmer TTS

    Then all audio parts are combined
    while keeping the original order.
    """

    # Detect English / Khmer parts
    parts = detect_language(text)

    # Empty audio that we will keep adding to
    final_audio = AudioSegment.empty()

    for part in parts:

        language = part["language"]
        text_part = part["text"].strip()

        # Ignore empty text
        if not text_part:
            continue

        # Ignore punctuation-only text
        #
        # Examples that will be ignored:
        # "."
        # ","
        # "!"
        # "?"
        #
        # But these will NOT be ignored:
        # "Hello"
        # "123"
        # "សួស្តី"
        if not re.search(
            r"[A-Za-z0-9\u1780-\u17FF]",
            text_part
        ):
            continue

        print("--------------------------------")
        print(f"Language: {language}")
        print(f"Text: {text_part}")

        # Create a temporary filename
        temp_filename = (
            f"temp_{uuid.uuid4()}.mp3"
        )

        try:

            # =========================
            # English TTS
            # =========================

            if language == "en":

                tts = gTTS(
                    text=text_part,
                    lang="en"
                )

            # =========================
            # Khmer TTS
            # =========================

            elif language == "km":

                tts = gTTS(
                    text=text_part,
                    lang="km"
                )

            # Unknown language
            else:
                print(
                    f"Skipping unsupported language: {language}"
                )
                continue

            # Generate temporary MP3
            tts.save(temp_filename)

            # Load generated MP3
            audio = AudioSegment.from_mp3(
                temp_filename
            )

            # Add this audio to the final audio
            final_audio += audio

        finally:

            # Delete temporary file
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    # =========================
    # Create final MP3 filename
    # =========================

    output_filename = (
        f"audio_{uuid.uuid4()}.mp3"
    )

    output_path = os.path.join(
        AUDIO_DIR,
        output_filename
    )

    # Export final combined audio
    final_audio.export(
        output_path,
        format="mp3"
    )

    print("--------------------------------")
    print("Audio generated successfully!")
    print(f"Output: {output_path}")
    print("--------------------------------")

    return output_filename