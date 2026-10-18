import json
import os

# Disable oneDNN/MKLDNN to avoid PaddlePaddle CPU issues
os.environ["FLAGS_enable_pir_api"] = "0"
os.environ["FLAGS_use_mkldnn"] = "0"

from paddleocr import PaddleOCR


ocr = PaddleOCR(
    lang="en",
    enable_mkldnn=False
)


def extract_text(image_path: str) -> str:

    result = ocr.predict(image_path)

    texts = []

    for res in result:

        data = res.json

        if isinstance(data, str):
            data = json.loads(data)

        result_data = data.get("res", data)

        rec_texts = result_data.get(
            "rec_texts",
            []
        )

        for text in rec_texts:

            text = text.strip()

            if text:
                texts.append(text)

    return "\n".join(texts)