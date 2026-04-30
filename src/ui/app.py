from __future__ import annotations

import customtkinter as ctk

from core import translate


class MorseApp(ctk.CTk):
	def __init__(self) -> None:
		super().__init__()
		ctk.set_appearance_mode("dark")

		self.title("Morse Code Translator")
		self.geometry("1100x700")
		self.minsize(900, 600)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)

		self.tabview = ctk.CTkTabview(self)
		self.tabview.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

		self.encoder_tab = self.tabview.add("Encoder")
		self.decoder_tab = self.tabview.add("Decoder")
		self.telegraph_tab = self.tabview.add("Telegraph")
		self.audio_tab = self.tabview.add("Audio")

		self._build_encoder_tab()
		self._build_decoder_tab()
		self._build_placeholder_tab(self.telegraph_tab, "Telegraph tools coming soon.")
		self._build_placeholder_tab(self.audio_tab, "Audio tools coming soon.")

	def _build_encoder_tab(self) -> None:
		self.encoder_tab.grid_columnconfigure(0, weight=1)
		self.encoder_tab.grid_rowconfigure(1, weight=1)
		self.encoder_tab.grid_rowconfigure(4, weight=1)

		ctk.CTkLabel(self.encoder_tab, text="Text Input").grid(
			row=0, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		self.encoder_input = ctk.CTkTextbox(self.encoder_tab, height=120)
		self.encoder_input.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

		ctk.CTkButton(self.encoder_tab, text="Encode", command=self._on_encode).grid(
			row=2, column=0, sticky="w", padx=10, pady=(0, 10)
		)

		ctk.CTkLabel(self.encoder_tab, text="Morse Output").grid(
			row=3, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		self.encoder_output = ctk.CTkTextbox(self.encoder_tab, height=120)
		self.encoder_output.grid(row=4, column=0, sticky="nsew", padx=10, pady=(0, 10))
		self._set_text(self.encoder_output, "")

	def _build_decoder_tab(self) -> None:
		self.decoder_tab.grid_columnconfigure(0, weight=1)
		self.decoder_tab.grid_rowconfigure(1, weight=1)
		self.decoder_tab.grid_rowconfigure(4, weight=1)

		ctk.CTkLabel(self.decoder_tab, text="Morse Input").grid(
			row=0, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		self.decoder_input = ctk.CTkTextbox(self.decoder_tab, height=120)
		self.decoder_input.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

		ctk.CTkButton(self.decoder_tab, text="Decode", command=self._on_decode).grid(
			row=2, column=0, sticky="w", padx=10, pady=(0, 10)
		)

		ctk.CTkLabel(self.decoder_tab, text="Text Output").grid(
			row=3, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		self.decoder_output = ctk.CTkTextbox(self.decoder_tab, height=120)
		self.decoder_output.grid(row=4, column=0, sticky="nsew", padx=10, pady=(0, 10))
		self._set_text(self.decoder_output, "")

	def _build_placeholder_tab(self, tab: ctk.CTkFrame, message: str) -> None:
		tab.grid_columnconfigure(0, weight=1)
		ctk.CTkLabel(tab, text=message).grid(row=0, column=0, padx=10, pady=10, sticky="w")

	def _get_text(self, textbox: ctk.CTkTextbox) -> str:
		return textbox.get("1.0", "end").strip()

	def _set_text(self, textbox: ctk.CTkTextbox, text: str) -> None:
		textbox.configure(state="normal")
		textbox.delete("1.0", "end")
		textbox.insert("1.0", text)
		textbox.configure(state="disabled")

	def _on_encode(self) -> None:
		text = self._get_text(self.encoder_input)
		if not text:
			self._set_text(self.encoder_output, "Enter text to encode.")
			return
		result, _ = translate(text, "encode")
		self._set_text(self.encoder_output, result)

	def _on_decode(self) -> None:
		text = self._get_text(self.decoder_input)
		if not text:
			self._set_text(self.decoder_output, "Enter Morse to decode.")
			return
		result, _ = translate(text, "decode")
		self._set_text(self.decoder_output, result)


def run() -> None:
	app = MorseApp()
	app.mainloop()
