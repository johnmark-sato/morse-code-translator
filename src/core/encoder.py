from __future__ import annotations

from typing import List, Tuple

from core.tree import ENCODE_MAP, MORSE_TREE, MorseNode, walk_path


def encode(text: str) -> Tuple[str, List[MorseNode]]:
	"""Encode text into Morse code.

	Returns the encoded string and the ordered list of visited nodes.
	"""
	if not text:
		return "", []

	words = text.strip().upper().split()
	if not words:
		return "", []

	encoded_words: List[str] = []
	node_path: List[MorseNode] = []

	for word in words:
		letters: List[str] = []
		for ch in word:
			code = ENCODE_MAP.get(ch)
			if code is None:
				letters.append("?")
				continue
			letters.append(code)
			node, nodes = walk_path(MORSE_TREE, code)
			if node is not None:
				node_path.extend(nodes)
		encoded_words.append(" ".join(letters))

	return " / ".join(encoded_words), node_path
