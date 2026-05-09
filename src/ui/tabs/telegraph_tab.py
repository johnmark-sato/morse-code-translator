import customtkinter as ctk
from core.telegraph import TelegraphSession

# === TELEGRAPH UI START ===

def build_telegraph_tab(parent: ctk.CTkFrame) -> None:

    # Configure layout
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_rowconfigure(0, weight=1)
    
    # Create session
    session = TelegraphSession()
    
    # Main frame
    main_frame = ctk.CTkFrame(parent)
    main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_rowconfigure(3, weight=1)
    
    # Current Morse Label
    current_label = ctk.CTkLabel(main_frame, text="Current Morse")
    current_label.grid(row=0,column=0,sticky="w",pady=(0,5))
    
    current_morse_box = ctk.CTkTextbox(main_frame, height=60)
    current_morse_box.grid(row=0,column=0,sticky="nsew", pady=(0,15))
    current_morse_box.configure(state="disabled")
    
    # Decoded Text Label
    decoded_label = ctk.CTkLabel(main_frame, text="Decoded Text")
    decoded_label.grid(row=0,column=0,sticky="w",pady=(0,5))
    
    decoded_text_box = ctk.CTkTextbox(main_frame)
    decoded_text_box.grid(row=0,column=0,sticky="nsew",pady=(0,15))
    decoded_text_box.configure(state="disabled")
    
    #Help Text
    help_label = ctk.CTkLabel(
        main_frame,
        text="Left Arrow = dot(.) | Right Arrow = dash(-) | Space = Commit"
    )
    help_label.grid(row=0,column=0,pady=(0,10))
    
    