from unittest import TestCase
from team import Team
from datetime import date


class TeamTestCase(TestCase):
    def setUp(self) -> None:
        self.name = "Boca Juniors"
        self.date = date(year=1908, month=2, day=5)

    def test_create_team(self):
        team_instance = Team(name=self.name,
                             foundation=self.date)
        self.assertIsNotNone(team_instance)
        self.assertEqual(team_instance.team_name, self.name)
        self.assertEqual(team_instance.foundation, self.date)

    def test_create_team_no_name_raise_TypeError(self):
        with self.assertRaises(TypeError):
            team_instance = Team(foundation=self.date)