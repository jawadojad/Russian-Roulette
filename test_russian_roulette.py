import unittest
from unittest.mock import patch, MagicMock
import tkinter
from russian_roulette import start_game, challenge_1

class TestRussianRouletteGame(unittest.TestCase):

    @patch('russian_roulette.messagebox.showinfo')
    @patch('russian_roulette.input', side_effect=['\n', 'print("Hello, World!")'])
    def test_start_game_correct_code(self, mock_input, mock_messagebox):
        with patch('builtins.print') as mock_print:
            start_game()
            # Check if the correct messages were printed
            self.assertIn(("Correct! You have survived this round."), [call[0][0] for call in mock_print.call_args_list])

    @patch('russian_roulette.messagebox.showinfo')
    @patch('russian_roulette.input', side_effect=['\n', 'print("Hello World!')])
    def test_start_game_incorrect_code(self, mock_input, mock_messagebox):
        with patch('builtins.print') as mock_print:
            start_game()
            # Check if the error message was printed
            self.assertIn(("Error: EOL while scanning string literal"), [call[0][0] for call in mock_print.call_args_list])
            self.assertIn(("Incorrect! You did not survive this round."), [call[0][0] for call in mock_print.call_args_list])

    @patch('russian_roulette.messagebox.showinfo')
    @patch('russian_roulette.input', side_effect=['\n', 'print(Hello, World!)'])
    def test_start_game_syntax_error(self, mock_input, mock_messagebox):
        with patch('builtins.print') as mock_print:
            start_game()
            # Check if the syntax error message was printed
            self.assertIn(("Error: invalid syntax"), [call[0][0] for call in mock_print.call_args_list])
            self.assertIn(("Incorrect! You did not survive this round."), [call[0][0] for call in mock_print.call_args_list])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
