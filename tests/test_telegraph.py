# === TELEGRAPH CORE START ===
import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from core.telegraph import TelegraphSession


class TestTelegraphSession(unittest.TestCase):
    def test_one_dot_commits_to_e(self) -> None:
        session = TelegraphSession()
        session.add_dot()
        session.commit_character()
        self.assertEqual(session.decoded_text, "E")
        self.assertEqual(session.current_symbols, "")

    def test_one_dash_commits_to_t(self) -> None:
        session = TelegraphSession()
        session.add_dash()
        session.commit_character()
        self.assertEqual(session.decoded_text, "T")
        self.assertEqual(session.current_symbols, "")

    def test_dot_dash_commits_to_a(self) -> None:
        session = TelegraphSession()
        session.add_dot()
        session.add_dash()
        session.commit_character()
        self.assertEqual(session.decoded_text, "A")
        self.assertEqual(session.current_symbols, "")

    def test_three_dots_commits_to_s(self) -> None:
        session = TelegraphSession()
        session.add_dot()
        session.add_dot()
        session.add_dot()
        session.commit_character()
        self.assertEqual(session.decoded_text, "S")
        self.assertEqual(session.current_symbols, "")

    def test_space_commits_current_character(self) -> None:
        session = TelegraphSession()
        session.add_dot()
        session.add_space()
        self.assertEqual(session.decoded_text, "E ")
        self.assertEqual(session.current_symbols, "")

    def test_reset_clears_state(self) -> None:
        session = TelegraphSession()
        session.add_dot()
        session.add_dash()
        session.commit_character()
        session.reset()
        self.assertEqual(session.decoded_text, "")
        self.assertEqual(session.current_symbols, "")


if __name__ == "__main__":
    unittest.main()
# === TELEGRAPH CORE END ===
