from __future__ import annotations

import time
import tkinter as tk

import customtkinter as ctk

from core import translate
from core.tree import MORSE_TABLE
from ui.visualizer import MorseTreeVisualizer


class MorseApp(ctk.CTk):
	def __init__(self) -> None:
		super().__init__()
		ctk.set_appearance_mode("dark")

		self.title("Morse Code Translator")
		self.geometry("1100x700")
		self.minsize(900, 600)
		self.after(50, lambda: self.state("zoomed"))

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
		self._build_menus()

	def _build_encoder_tab(self) -> None:
		self.encoder_tab.grid_columnconfigure(0, weight=1)
		self.encoder_tab.grid_rowconfigure(0, weight=1)

		self.encoder_pane = tk.PanedWindow(
			self.encoder_tab,
			orient="horizontal",
			sashrelief="raised",
			bg="#12161c",
		)
		self.encoder_pane.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

		left_frame = ctk.CTkFrame(self.encoder_pane, fg_color="transparent")
		left_frame.grid_columnconfigure(0, weight=1)
		left_frame.grid_rowconfigure(1, weight=1)
		left_frame.grid_rowconfigure(4, weight=1)

		self.encoder_side = ctk.CTkFrame(self.encoder_pane)
		self.encoder_side.grid_columnconfigure(0, weight=1)
		self.encoder_side.grid_rowconfigure(0, weight=1)
		self.encoder_side_inner = ctk.CTkScrollableFrame(self.encoder_side)
		self.encoder_side_inner.grid(row=0, column=0, sticky="nsew")
		self.encoder_side_inner.grid_columnconfigure(0, weight=1)
		self.encoder_side_inner.grid_rowconfigure(0, weight=1)
		self.encoder_side_inner.grid_rowconfigure(1, weight=1)

		self.encoder_pane.add(left_frame, minsize=420)
		self.encoder_pane.add(self.encoder_side, minsize=280)

		ctk.CTkLabel(left_frame, text="Text Input").grid(
			row=0, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		self.encoder_input = ctk.CTkTextbox(left_frame, height=120)
		self.encoder_input.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

		ctk.CTkButton(left_frame, text="Encode", command=self._on_encode).grid(
			row=2, column=0, sticky="w", padx=10, pady=(0, 10)
		)

		ctk.CTkLabel(left_frame, text="Morse Output").grid(
			row=3, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		self.encoder_output = ctk.CTkTextbox(left_frame, height=120)
		self.encoder_output.grid(row=4, column=0, sticky="nsew", padx=10, pady=(0, 10))
		self._set_text(self.encoder_output, "")

		self.encoder_visualizer = MorseTreeVisualizer(self.encoder_side_inner)
		self.encoder_visualizer.grid(row=0, column=0, sticky="nsew", padx=4, pady=(4, 2))
		self.encoder_guide = self._build_morse_guide(self.encoder_side_inner)
		self.encoder_guide.grid(row=1, column=0, sticky="nsew", padx=4, pady=(2, 4))
		self.encoder_visualizer.grid_remove()
		self.encoder_guide.grid_remove()
		self.encoder_pane.forget(self.encoder_side)
		self.encoder_panels = [self.encoder_visualizer, self.encoder_guide]
		self.after(80, lambda: self._set_pane_ratio(self.encoder_pane, 0.6))

	def _build_decoder_tab(self) -> None:
		self.decoder_tab.grid_columnconfigure(0, weight=1)
		self.decoder_tab.grid_rowconfigure(0, weight=1)

		self.decoder_pane = tk.PanedWindow(
			self.decoder_tab,
			orient="horizontal",
			sashrelief="raised",
			bg="#12161c",
		)
		self.decoder_pane.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

		left_frame = ctk.CTkFrame(self.decoder_pane, fg_color="transparent")
		left_frame.grid_columnconfigure(0, weight=1)
		left_frame.grid_rowconfigure(1, weight=1)
		left_frame.grid_rowconfigure(4, weight=1)

		self.decoder_side = ctk.CTkFrame(self.decoder_pane)
		self.decoder_side.grid_columnconfigure(0, weight=1)
		self.decoder_side.grid_rowconfigure(0, weight=1)
		self.decoder_side_inner = ctk.CTkScrollableFrame(self.decoder_side)
		self.decoder_side_inner.grid(row=0, column=0, sticky="nsew")
		self.decoder_side_inner.grid_columnconfigure(0, weight=1)
		self.decoder_side_inner.grid_rowconfigure(0, weight=1)
		self.decoder_side_inner.grid_rowconfigure(1, weight=1)

		self.decoder_pane.add(left_frame, minsize=420)
		self.decoder_pane.add(self.decoder_side, minsize=280)

		ctk.CTkLabel(left_frame, text="Morse Input").grid(
			row=0, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		self.decoder_input = ctk.CTkTextbox(left_frame, height=120)
		self.decoder_input.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

		ctk.CTkButton(left_frame, text="Decode", command=self._on_decode).grid(
			row=2, column=0, sticky="w", padx=10, pady=(0, 10)
		)

		ctk.CTkLabel(left_frame, text="Text Output").grid(
			row=3, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		self.decoder_output = ctk.CTkTextbox(left_frame, height=120)
		self.decoder_output.grid(row=4, column=0, sticky="nsew", padx=10, pady=(0, 10))
		self._set_text(self.decoder_output, "")

		self.decoder_visualizer = MorseTreeVisualizer(self.decoder_side_inner)
		self.decoder_visualizer.grid(row=0, column=0, sticky="nsew", padx=4, pady=(4, 2))
		self.decoder_guide = self._build_morse_guide(self.decoder_side_inner)
		self.decoder_guide.grid(row=1, column=0, sticky="nsew", padx=4, pady=(2, 4))
		self.decoder_visualizer.grid_remove()
		self.decoder_guide.grid_remove()
		self.decoder_pane.forget(self.decoder_side)
		self.decoder_panels = [self.decoder_visualizer, self.decoder_guide]
		self.after(80, lambda: self._set_pane_ratio(self.decoder_pane, 0.6))

	def _build_placeholder_tab(self, tab: ctk.CTkFrame, message: str) -> None:
		tab.grid_columnconfigure(0, weight=1)
		ctk.CTkLabel(tab, text=message).grid(row=0, column=0, padx=10, pady=10, sticky="w")

	def _build_menus(self) -> None:
		self.menu_bar = tk.Menu(self)
		file_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.animation_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.menu_bar.add_cascade(label="File", menu=file_menu)
		self.menu_bar.add_cascade(label="View", menu=self.view_menu)
		self.menu_bar.add_cascade(label="Animation", menu=self.animation_menu)
		self.config(menu=self.menu_bar)

		file_menu.add_command(label="Exit", command=self.destroy)

		self.encoder_visual_var = tk.BooleanVar(value=False)
		self.encoder_guide_var = tk.BooleanVar(value=False)
		self.decoder_visual_var = tk.BooleanVar(value=False)
		self.decoder_guide_var = tk.BooleanVar(value=False)
		self.animation_speed_var = tk.StringVar(value="normal")

		self.view_menu.add_checkbutton(
			label="Encoder: Visualizer",
			variable=self.encoder_visual_var,
			command=self._toggle_encoder_visual,
		)
		self.view_menu.add_checkbutton(
			label="Encoder: Guide",
			variable=self.encoder_guide_var,
			command=self._toggle_encoder_guide,
		)
		self.view_menu.add_separator()
		self.view_menu.add_checkbutton(
			label="Decoder: Visualizer",
			variable=self.decoder_visual_var,
			command=self._toggle_decoder_visual,
		)
		self.view_menu.add_checkbutton(
			label="Decoder: Guide",
			variable=self.decoder_guide_var,
			command=self._toggle_decoder_guide,
		)

		self.animation_menu.add_radiobutton(
			label="Slow",
			value="slow",
			variable=self.animation_speed_var,
		)
		self.animation_menu.add_radiobutton(
			label="Normal",
			value="normal",
			variable=self.animation_speed_var,
		)
		self.animation_menu.add_radiobutton(
			label="Fast",
			value="fast",
			variable=self.animation_speed_var,
		)
		self.animation_menu.add_separator()
		self.animation_menu.add_radiobutton(
			label="Real-time",
			value="realtime",
			variable=self.animation_speed_var,
		)

	def _resolve_animation_delay(self, elapsed_seconds: float, step_count: int) -> int:
		mode = self.animation_speed_var.get()
		speed_map = {
			"slow": 600,
			"normal": 350,
			"fast": 150,
		}
		if mode == "realtime":
			if step_count <= 0:
				return 0
			return max(10, int((elapsed_seconds * 1000) / step_count))
		return speed_map.get(mode, 350)

	def _set_panel_visibility(
		self,
		pane: tk.PanedWindow,
		side_frame: ctk.CTkFrame,
		panel: ctk.CTkFrame,
		panels: list[ctk.CTkFrame],
		visible: bool,
	) -> None:
		if visible:
			self._ensure_side_pane(pane, side_frame, True)
			panel.grid()
		else:
			panel.grid_remove()

		self._sync_side_panel(pane, side_frame, panels, force_visible=visible)

	def _sync_side_panel(
		self,
		pane: tk.PanedWindow,
		side_frame: ctk.CTkFrame,
		panels: list[ctk.CTkFrame],
		force_visible: bool | None = None,
	) -> None:
		self.update_idletasks()
		any_visible = any(panel.winfo_ismapped() for panel in panels)
		if force_visible is True:
			any_visible = True
		self._ensure_side_pane(pane, side_frame, any_visible)

	def _sync_menu_var(self, var: tk.BooleanVar, panel: ctk.CTkFrame) -> None:
		self.after_idle(lambda: var.set(panel.winfo_ismapped()))

	def _ensure_side_pane(self, pane: tk.PanedWindow, side_frame: ctk.CTkFrame, show: bool) -> None:
		panes = pane.panes()
		side_name = str(side_frame)
		if show and side_name not in panes:
			pane.add(side_frame, minsize=280)
			self.after(50, lambda: self._set_pane_ratio(pane, 0.6))
		elif not show and side_name in panes:
			pane.forget(side_frame)

	def _set_pane_ratio(self, pane: tk.PanedWindow, ratio: float) -> None:
		width = pane.winfo_width()
		if width < 2:
			self.after(60, lambda: self._set_pane_ratio(pane, ratio))
			return
		pane.sash_place(0, int(width * ratio), 0)

	def _toggle_encoder_visual(self) -> None:
		self._set_panel_visibility(
			self.encoder_pane,
			self.encoder_side,
			self.encoder_visualizer,
			self.encoder_panels,
			self.encoder_visual_var.get(),
		)
		self._sync_menu_var(self.encoder_visual_var, self.encoder_visualizer)

	def _toggle_encoder_guide(self) -> None:
		self._set_panel_visibility(
			self.encoder_pane,
			self.encoder_side,
			self.encoder_guide,
			self.encoder_panels,
			self.encoder_guide_var.get(),
		)
		self._sync_menu_var(self.encoder_guide_var, self.encoder_guide)

	def _toggle_decoder_visual(self) -> None:
		self._set_panel_visibility(
			self.decoder_pane,
			self.decoder_side,
			self.decoder_visualizer,
			self.decoder_panels,
			self.decoder_visual_var.get(),
		)
		self._sync_menu_var(self.decoder_visual_var, self.decoder_visualizer)

	def _toggle_decoder_guide(self) -> None:
		self._set_panel_visibility(
			self.decoder_pane,
			self.decoder_side,
			self.decoder_guide,
			self.decoder_panels,
			self.decoder_guide_var.get(),
		)
		self._sync_menu_var(self.decoder_guide_var, self.decoder_guide)

	def _build_morse_guide(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
		frame = ctk.CTkFrame(parent)
		frame.grid_columnconfigure(0, weight=1)
		frame.grid_rowconfigure(1, weight=1)
		ctk.CTkLabel(frame, text="Morse Guide").grid(
			row=0, column=0, sticky="w", padx=10, pady=(10, 4)
		)
		textbox = ctk.CTkTextbox(frame)
		textbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
		textbox.insert("1.0", self._format_morse_guide())
		textbox.configure(state="disabled", font=("Consolas", 12))
		return frame

	def _format_morse_guide(self) -> str:
		entries = [f"{char} {code}" for char, code in MORSE_TABLE.items()]
		lines = []
		row = []
		for entry in entries:
			row.append(entry.ljust(10))
			if len(row) == 4:
				lines.append("  ".join(row).rstrip())
				row = []
		if row:
			lines.append("  ".join(row).rstrip())
		return "\n".join(lines)

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
		start = time.perf_counter()
		result, node_path = translate(text, "encode")
		elapsed = time.perf_counter() - start
		self._set_text(self.encoder_output, result)
		if self.encoder_visualizer.winfo_ismapped():
			delay_ms = self._resolve_animation_delay(elapsed, len(node_path))
			self.encoder_visualizer.highlight_path(node_path, delay_ms=delay_ms)

	def _on_decode(self) -> None:
		text = self._get_text(self.decoder_input)
		if not text:
			self._set_text(self.decoder_output, "Enter Morse to decode.")
			return
		start = time.perf_counter()
		result, node_path = translate(text, "decode")
		elapsed = time.perf_counter() - start
		self._set_text(self.decoder_output, result)
		if self.decoder_visualizer.winfo_ismapped():
			delay_ms = self._resolve_animation_delay(elapsed, len(node_path))
			self.decoder_visualizer.highlight_path(node_path, delay_ms=delay_ms)


def run() -> None:
	app = MorseApp()
	app.mainloop()
