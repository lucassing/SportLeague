import os
from unittest import TestCase
import subprocess


class TournamentIntegrationTestCase(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        os.remove('output.txt')

    def test_integration_position(self):
        subprocess.run(['python', '.\main.py', 'tests/testfiles/test_integration.txt'])
        with open('output.txt', 'r') as f:
            self.assertNotEqual("", next(f))
