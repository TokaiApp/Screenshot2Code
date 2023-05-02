import sys
import os
from PIL import Image
import pytesseract as tess

os.environ['TESSDATA_PREFIX'] = '/Users/seth/opt/anaconda3/share/tessdata'

# Set the path to the Tesseract OCR executable
tess.pytesseract.tesseract_cmd = r'/opt/local/bin/tesseract'

'''
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
'''

def s2c(image_path):
    try:
        img = Image.open(image_path)

        # Custom Tesseract configuration for preserving whitespace and formatting
        config = r"-c preserve_interword_spaces=2 --psm 6"

        text = tess.image_to_string(img, config=config)

        # Post-process the extracted text to maintain indentation
        #processed_text = post_process(text)

        # Save the extracted code to a text file

        return text

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        image_path = sys.argv[1]
        output_path = sys.argv[2]

        text = s2c(image_path)
        with open(output_path, "w") as f:
            f.write(text)
    else:
        print("Usage: python screenshot2code.py <image_path>")