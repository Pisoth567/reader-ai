import os

# Disable oneDNN/MKLDNN to avoid PaddlePaddle PIR CPU issue
os.environ["FLAGS_enable_pir_api"] = "0"
os.environ["FLAGS_use_mkldnn"] = "0"

from paddleocr import PaddleOCR


ocr = PaddleOCR(
    lang="en",
    enable_mkldnn=False
)

image_path = "test.png"

result = ocr.predict(image_path)

for res in result:
    print(res)