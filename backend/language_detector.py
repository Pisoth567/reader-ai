def is_khmer(char):
    return "\u1780" <= char <= "\u17FF"


def detect_language(text):
    result = []

    current_language = None
    current_text = ""

    for char in text:

        # Detect Khmer character
        if is_khmer(char):
            language = "km"
        else:
            language = "en"

        # Language changed
        if current_language != language:

            if current_text:
                result.append({
                    "language": current_language,
                    "text": current_text
                })

            current_language = language
            current_text = char

        else:
            current_text += char

    # Add remaining text
    if current_text:
        result.append({
            "language": current_language,
            "text": current_text
        })

    return result


text = "Hello, my name is នេត ពិសុទ្ធ. I am a Computer Science student."

parts = detect_language(text)

for part in parts:
    print(part)