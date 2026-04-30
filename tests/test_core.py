import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from core.decoder import decode
from core.encoder import encode
from core.tree import MORSE_TABLE


class TestMorseCore(unittest.TestCase):
    def test_encode_decode_table(self) -> None:
        for char, code in MORSE_TABLE.items():
            encoded, _ = encode(char)
            self.assertEqual(encoded, code)
            decoded, _ = decode(code)
            self.assertEqual(decoded, char)

    def test_empty(self) -> None:
        encoded, path = encode("")
        self.assertEqual(encoded, "")
        self.assertEqual(path, [])
        decoded, path = decode("")
        self.assertEqual(decoded, "")
        self.assertEqual(path, [])

    def test_word_gap(self) -> None:
        encoded, _ = encode("HI HI")
        self.assertIn(" / ", encoded)
        decoded, _ = decode(".... .. / .... ..")
        self.assertEqual(decoded, "HI HI")

    def test_unknown(self) -> None:
        encoded, _ = encode("@")
        self.assertEqual(encoded, "?")
        decoded, _ = decode("..--")
        self.assertEqual(decoded, "?")

    def test_sos(self) -> None:
        encoded, _ = encode("SOS")
        self.assertEqual(encoded, "... --- ...")
        decoded, _ = decode("... --- ...")
        self.assertEqual(decoded, "SOS")


if __name__ == "__main__":
    unittest.main()
