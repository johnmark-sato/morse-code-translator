"""Core translation API."""

from core.encoder import encode
from core.decoder import decode
from core.telegraph import TelegraphSession


def translate(value: str, mode: str):
    """Translate text to Morse or Morse to text.

    Args:
        value: Input text or Morse string.
        mode: "encode" or "decode".

    Returns:
        Tuple of (result, node_path).
    """
    if mode == "encode":
        return encode(value)
    if mode == "decode":
        return decode(value)
    raise ValueError("mode must be 'encode' or 'decode'")


__all__ = ["encode", "decode", "translate", "TelegraphSession"]
