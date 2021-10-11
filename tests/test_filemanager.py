import sys
from unittest import TestCase
from unittest.mock import patch
from filemanager import TournamentFileManager


class TournamentFileManagerTestCase(TestCase):

    def setUp(self) -> None:
        pass

    def test_empty_file(self):
        test_args = ["", "tests/testfiles/test_empty.txt"]
        with patch.object(sys, 'argv', test_args):
            tournament_file_manager = TournamentFileManager()
            teams_data = tournament_file_manager.extract_teams_data()
            games_data = tournament_file_manager.extract_games_data()
            self.assertEqual(teams_data, set())
            self.assertEqual(games_data, [])

    def test_valid_file(self):
        test_args = ["", "tests/testfiles/test_valid_data.txt"]
        with patch.object(sys, 'argv', test_args):
            tournament_file_manager = TournamentFileManager()
            teams_data = tournament_file_manager.extract_teams_data()
            games_data = tournament_file_manager.extract_games_data()
            self.assertEqual(teams_data, {'Fantastics', 'Crazy Ones', 'Rebels', 'FC Super'})
            self.assertNotEqual(games_data, [])
