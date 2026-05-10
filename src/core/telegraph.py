from core.decoder import decode

# === TELEGRAPH CORE START ===

class TelegraphSession:
    def __init__(self) -> None:
        self.current_symbols = ""
        self.decoded_text = ""

    def add_dot(self):
        self.current_symbols += "."
        return self.get_state()

    def add_dash(self):
        self.current_symbols += "-"
        return self.get_state()

    def commit_character(self):
        if not self.current_symbols:
            return self.get_state()

        decoded_char, _ = decode(self.current_symbols)
        self.decoded_text += decoded_char
        self.current_symbols = ""
        return self.get_state()

    def add_space(self):
        self.commit_character()
        if not self.decoded_text.endswith(" "):
            self.decoded_text += " "
        return self.get_state()

    def reset(self):
        self.current_symbols = ""
        self.decoded_text = ""
        return self.get_state()

    def get_state(self):
        return {
            "current_symbols": self.current_symbols,
            "decoded_text": self.decoded_text,
        }

# === TELEGRAPH CORE END ===
