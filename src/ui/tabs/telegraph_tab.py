import customtkinter as ctk
from core.telegraph import TelegraphSession

# === TELEGRAPH UI START ===

def build_telegraph_tab(parent: ctk.CTkFrame) -> None:

    # Configure layout
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_rowconfigure(0, weight=1)
    
    # Create session
    session = TelegraphSession()
    
  