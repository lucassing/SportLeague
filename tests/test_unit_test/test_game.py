from unittest import TestCase
from team import Team
from game import TeamGameData, Game
from datetime import date


class TestTeamGameData(TestCase):
    def setUp(self) -> None:
        self.team = Team(name="Boca Juniors")

    def test_create_TeamGameData(self):
        instance = TeamGameData(team=self.team,
                                scored=3)

        self.assertIsNotNone(instance)
        self.assertEqual(instance.team, self.team)
        self.assertEqual(instance.score, 3)

    def test_create_TeamGameData_no_team_raise_TypeError(self):
        with self.assertRaises(TypeError):
            team_instance = TeamGameData(scored=3)

    def test_create_TeamGameData_no_scored_raise_TypeError(self):
        with self.assertRaises(TypeError):
            team_instance = Team(team=self.team)


class TestGame(TestCase):
    def setUp(self) -> None:
        self.team_one = Team(name="Boca Juniors")
        self.team_two = Team(name="River Plate")

        self.team_game_data_one = TeamGameData(team=self.team_one,
                                               scored=3)
        self.team_game_data_two = TeamGameData(team=self.team_two,
                                               scored=0)

    def test_create_game(self):
        instance = Game(game_data=[self.team_game_data_one, self.team_game_data_two])

        self.assertIsNotNone(instance)
        self.assertEqual(instance.winner, self.team_one)
        self.assertEqual(instance.is_draw, False)
        self.assertEqual(instance.teams, [self.team_one, self.team_two])

    def test_is_draw(self):
        self.team_game_data_one.score = self.team_game_data_two.score
        game_data = [self.team_game_data_one, self.team_game_data_two]
        instance = Game(game_data=game_data)

        self.assertIsNone(instance.winner)
        self.assertTrue(instance.is_draw)

