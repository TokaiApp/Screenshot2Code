import os
import shutil
import sys
from typing import Tuple

import pandas as pd
import pytesseract as tess
from guesslang import Guess
from PIL import Image
from pytesseract import Output


class Screenshot2Code:
    # Set the path to the Tesseract OCR executable
    @staticmethod
    def check_for_tesseract() -> bool:
        tess_cmd = shutil.which("tesseract")
        if tess_cmd is not None:
            tess.pytesseract.tesseract_cmd = tess_cmd
            return True
        return False

    # FIXME: enforce dealing with the TESSDATA_PREFIX prefix
    @staticmethod
    def check_for_tessdata_prefix():
        if os.environ.get("TESSDATA_PREFIX"):
            print("TESSDATA_PREFIX has been defined", file=sys.stderr)
        else:
            # not sure how to deal with this yet
            os.environ["TESSDATA_PREFIX"] = "./tess_data_bak"
        return True

    # FIXME: sometime the space formatting is very wrong
    @staticmethod
    def preserve_identation(frame: pd.DataFrame) -> str:
        df1 = frame[(frame.conf != "-1") & (frame.text != " ") & (frame.text != "")]

        # sort blocks vertically
        code = ""
        sorted_blocks = (
            df1.groupby("block_num").first().sort_values("top").index.tolist()
        )
        for block in sorted_blocks:
            curr = df1[df1["block_num"] == block]
            sel = curr[curr.text.str.len() > 3]
            char_w = (sel.width / sel.text.str.len()).mean()
            prev_par, prev_line, prev_left = 0, 0, 0
            text = ""
            for ix, ln in curr.iterrows():
                # add new line when necessary
                if prev_par != ln["par_num"]:
                    text += "\n"
                    prev_par = ln["par_num"]
                    prev_line = ln["line_num"]
                    prev_left = 0
                elif prev_line != ln["line_num"]:
                    text += "\n"
                    prev_line = ln["line_num"]
                    prev_left = 0

                added = 0  # num of spaces that should be added
                if ln["left"] / char_w > prev_left + 1:
                    added = int((ln["left"]) / char_w) - prev_left
                    text += " " * 2 * added  # go extra on identation by default
                text += ln["text"] + " "
                prev_left += len(ln["text"]) + added + 1
            text += "\n"
            code += text

        return code

    @staticmethod
    def guess_lang(text_in: str) -> str | None:
        print(text_in, file=sys.stderr)
        guess = Guess()
        name = guess.language_name(text_in)
        print(name, file=sys.stderr)
        return name

    def convert(self, image_path: str) -> Tuple[str | None, str | None]:
        try:
            img = Image.open(image_path)

            # Custom Tesseract configuration for preserving whitespace and formatting
            config = r"-c preserve_interword_spaces=1 --psm 6 --oem 3"

            text_data = tess.image_to_data(img, config=config, output_type=Output.DICT)
            # print(text_data)
            frame = pd.DataFrame(text_data)
            # print("------------------------------")
            # print(frame)
            text = self.preserve_identation(frame)

            # Post-process the extracted text to maintain indentation
            # processed_text = post_process(text)

            # Save the extracted code to a text file
            lang = self.guess_lang(text)

            return lang, text

        except Exception as e:
            print("Error:", str(e))
            return None, None


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


if __name__ == "__main__":
    S2C = Screenshot2Code()
    if S2C.check_for_tesseract() is False:
        print("Please make sure you have tesseract installed.", file=sys.stderr)
        exit(1)
    S2C.check_for_tessdata_prefix()

    if len(sys.argv) == 3:
        image_path = sys.argv[1]
        output_path = sys.argv[2]

        lang, text = S2C.convert(image_path)
        with open(output_path, "w") as f:
            if text:
                f.write(text)
    else:
        print("Usage: python screenshot2code.py <screenshot_path> <output_path>")
