from __future__ import annotations

from typing import Iterable, Tuple

import numpy as np
import sounddevice as sd

DEFAULT_SAMPLE_RATE = 44100
DEFAULT_FREQUENCY = 700.0


def stop_playback() -> None:
    sd.stop()


def play_wave(wave: np.ndarray, sample_rate: int = DEFAULT_SAMPLE_RATE) -> None:
    if wave.size == 0:
        return
    sd.play(wave, sample_rate)


def build_morse_wave(
    morse: str,
    unit_seconds: float,
    volume: float,
    frequency: float = DEFAULT_FREQUENCY,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
) -> Tuple[np.ndarray, int]:
    text = morse.strip()
    if not text:
        return np.zeros(0, dtype=np.float32), sample_rate

    unit = max(0.01, unit_seconds)
    dot = unit
    dash = unit * 3.0
    intra_gap = unit
    letter_gap = unit * 3.0
    word_gap = unit * 7.0

    tokens = text.replace("/", " / ").split()
    segments = []

    for index, token in enumerate(tokens):
        if token == "/":
            segments.append(_silence(word_gap, sample_rate))
            continue
        for char_index, symbol in enumerate(token):
            if symbol == ".":
                segments.append(_tone(dot, frequency, sample_rate, volume))
            elif symbol == "-":
                segments.append(_tone(dash, frequency, sample_rate, volume))
            if char_index < len(token) - 1:
                segments.append(_silence(intra_gap, sample_rate))
        if index < len(tokens) - 1 and tokens[index + 1] != "/":
            segments.append(_silence(letter_gap, sample_rate))

    if not segments:
        return np.zeros(0, dtype=np.float32), sample_rate

    return np.concatenate(segments), sample_rate


def _tone(duration: float, frequency: float, sample_rate: int, volume: float) -> np.ndarray:
    if duration <= 0:
        return np.zeros(0, dtype=np.float32)
    length = int(sample_rate * duration)
    t = np.linspace(0, duration, length, endpoint=False)
    wave = np.sin(2.0 * np.pi * frequency * t) * volume
    return wave.astype(np.float32)


def _silence(duration: float, sample_rate: int) -> np.ndarray:
    if duration <= 0:
        return np.zeros(0, dtype=np.float32)
    return np.zeros(int(sample_rate * duration), dtype=np.float32)


def sanitize_morse_symbols(text: str) -> str:
    allowed = {".", "-", "/", " "}
    return "".join(ch for ch in text if ch in allowed)
