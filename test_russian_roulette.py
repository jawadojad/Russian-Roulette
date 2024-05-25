import unittest
from unittest.mock import patch
from russian_roulette import start_game, challenge_1

class TestRussianRouletteGame(unittest.TestCase):

    @patch('tkinter.messagebox.showinfo')
    @patch('builtins.input', side_effect=['\n', 'print("Hello, World!")'])
    def test_challenge_1_correct_code(self, mock_input, mock_messagebox_showinfo):
        with patch('builtins.print') as mock_print:
            challenge_1()
            # Check if the success message was shown
            mock_messagebox_showinfo.assert_called_with("Result", "Correct! You have survived this round.")

    @patch('tkinter.messagebox.showerror')
    @patch('builtins.input', side_effect=['\n', 'print(Hello, World!)'])  # Intentional syntax error
    def test_challenge_1_syntax_error(self, mock_input, mock_messagebox_showerror):
        with patch('builtins.print') as mock_print:
            challenge_1()
            # Check if the syntax error message was shown
            mock_messagebox_showerror.assert_called()

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
