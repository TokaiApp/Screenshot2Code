import os
import shutil
import sys

import pytesseract as tess
from guesslang import Guess
from PIL import Image

# os.environ["TESSDATA_PREFIX"] = "/Users/seth/opt/anaconda3/share/tessdata"


# Set the path to the Tesseract OCR executable
def check_for_tesseract():
    tess_cmd = shutil.which("tesseract")
    if tess_cmd is not None:
        tess.pytesseract.tesseract_cmd = tess_cmd
        return True
    return False


def check_for_tessdata_prefix():
    if os.environ.get("TESSDATA_PREFIX"):
        print("TESSDATA_PREFIX has been defined")
    else:
        # not sure how to deal with this yet
        os.environ["TESSDATA_PREFIX"] = ""


"""
def post_process(text):
    lines = text.split('\n')
    processed_lines = []

    for line in lines:
        # Remove leading and trailing whitespaces
        stripped_line = line.strip()

        # Count the number of leading spaces
        leading_spaces = len(line) - len(stripped_line)

        # Replace leading spaces with the appropriate number of spaces for indentation
        indented_line = ' ' * leading_spaces + stripped_line
        processed_lines.append(indented_line)

    return '\n'.join(processed_lines)
"""


def guess_lang(text_in: str):
    guess = Guess()
    name = guess.language_name(text_in)
    print(name)


def s2c(image_path):
    try:
        img = Image.open(image_path)

        # Custom Tesseract configuration for preserving whitespace and formatting
        config = r"-c preserve_interword_spaces=2 --psm 6"

        text = tess.image_to_string(img, config=config)

        # Post-process the extracted text to maintain indentation
        # processed_text = post_process(text)

        # Save the extracted code to a text file
        guess_lang(text)

        return text

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    if check_for_tesseract() is False:
        print("Please make sure you have tesseract installed.")
        exit(1)
    check_for_tessdata_prefix()

    if len(sys.argv) == 3:
        image_path = sys.argv[1]
        output_path = sys.argv[2]

        text = s2c(image_path)
        with open(output_path, "w") as f:
            f.write(text)
    else:
        print("Usage: python screenshot2code.py <screenshot_path> <output_path>")
