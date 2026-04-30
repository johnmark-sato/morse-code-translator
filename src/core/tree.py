from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class MorseNode:
	char: str = ""
	dot: Optional["MorseNode"] = None
	dash: Optional["MorseNode"] = None


MORSE_TABLE: Dict[str, str] = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
}


def build_tree(table: Dict[str, str]) -> MorseNode:
	root = MorseNode("")
	for char, code in table.items():
		current = root
		for symbol in code:
			if symbol == ".":
				if current.dot is None:
					current.dot = MorseNode("")
				current = current.dot
			elif symbol == "-":
				if current.dash is None:
					current.dash = MorseNode("")
				current = current.dash
			else:
				raise ValueError(f"Invalid Morse symbol: {symbol}")
		current.char = char
	return root


def walk_path(root: MorseNode, code: str) -> Tuple[Optional[MorseNode], List[MorseNode]]:
	nodes: List[MorseNode] = [root]
	current: Optional[MorseNode] = root
	for symbol in code:
		if current is None:
			return None, nodes
		if symbol == ".":
			current = current.dot
		elif symbol == "-":
			current = current.dash
		else:
			return None, nodes
		if current is None:
			return None, nodes
		nodes.append(current)
	return current, nodes


MORSE_TREE = build_tree(MORSE_TABLE)
ENCODE_MAP = dict(MORSE_TABLE)
