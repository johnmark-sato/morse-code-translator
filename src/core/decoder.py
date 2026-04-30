from __future__ import annotations

import re
from typing import List, Tuple

from core.tree import MORSE_TREE, MorseNode, walk_path


def _tokenize(morse_str: str) -> List[str]:
	text = morse_str.strip()
	if not text:
		return []
	text = re.sub(r"\s{3,}", " / ", text)
	text = text.replace("/", " / ")
	return [token for token in text.split() if token]


def decode(morse_str: str) -> Tuple[str, List[MorseNode]]:
	"""Decode Morse code into text.

	Returns the decoded string and the ordered list of visited nodes.
	"""
	tokens = _tokenize(morse_str)
	if not tokens:
		return "", []

	result_chars: List[str] = []
	node_path: List[MorseNode] = []

	for token in tokens:
		if token == "/":
			if result_chars and result_chars[-1] != " ":
				result_chars.append(" ")
			continue
		node, nodes = walk_path(MORSE_TREE, token)
		node_path.extend(nodes)
		if node is None or not node.char:
			result_chars.append("?")
		else:
			result_chars.append(node.char)

	return "".join(result_chars).strip(), node_path
