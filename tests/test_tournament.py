from unittest import TestCase
from team import Team
from game import TeamGameData, Game
from tournament import Tournament


class TestTournament(TestCase):
    def setUp(self) -> None:
        self.teams = [Team(name="Boca Juniors"), Team(name="River Plate")]

        self.teams_game_data_one = [TeamGameData(team=self.teams[0],
                                                 scored=3),
                                    TeamGameData(team=self.teams[1],
                                                 scored=0)]
        self.teams_game_data_two = [TeamGameData(team=self.teams[0],
                                                 scored=1),
                                    TeamGameData(team=self.teams[1],
                                                 scored=1)
                                    ]
        self.game_one = Game(game_data=self.teams_game_data_one)
        self.game_two = Game(game_data=self.teams_game_data_two)

        self.tournament = Tournament(teams=self.teams)

    def test_create_Tournament(self):
        instance = Tournament(teams=self.teams, year=2021)

        self.assertIsNotNone(instance)
        self.assertEqual(instance.teams, self.teams)
        self.assertEqual(instance.year, 2021)

    def test_add_game(self):
        self.tournament.add_game(self.game_one)
        self.assertTrue(self.game_one in self.tournament.games)

    def test_add_bulk_game(self):
        bulk = [self.game_one, self.game_two]
        self.tournament.add_bulk_game(bulk)
        self.assertEqual(self.tournament.games, bulk)

    def test_stats(self):
        bulk = [self.game_one, self.game_two]
        self.tournament.add_bulk_game(bulk)
        self.tournament.stats()
        self.assertEqual(self.tournament.stats()[0], (self.teams[0], 4))
        self.assertEqual(self.tournament.stats()[1], (self.teams[1], 1))

    def test_str(self):
        self.assertEqual(str(self.tournament), "1 Boca Juniors 0 \n1 River Plate 0 \n")