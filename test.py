import os
import sys
import unittest
from contextlib import contextmanager

from screenshot2code import Screenshot2Code


@contextmanager
def nullify_output(suppress_stdout=True, suppress_stderr=True):
    stdout = sys.stdout
    stderr = sys.stderr
    devnull = open(os.devnull, "w")
    try:
        if suppress_stdout:
            sys.stdout = devnull
        if suppress_stderr:
            sys.stderr = devnull
        yield
    finally:
        if suppress_stdout:
            sys.stdout = stdout
        if suppress_stderr:
            sys.stderr = stderr


class TestS2C(unittest.TestCase):
    def setUp(self) -> None:
        self.S2C = Screenshot2Code()
        self.assertTrue(self.S2C.check_for_tessdata_prefix())

        return super().setUp()

    def test_lang(self):
        test_dir = "./screenshots/"
        for file in os.listdir(test_dir):
            with self.subTest():
                # with nullify_output(suppress_stdout=False, suppress_stderr=True):
                lang, _ = self.S2C.convert(test_dir + file)
                if lang:
                    self.assertEqual(lang.lower(), file[:-4])
                else:
                    print(f"Testing {lang} failed")


if __name__ == "__main__":
    unittest.main()
