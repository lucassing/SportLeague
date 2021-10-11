import fileinput
import re


class TournamentFileManager:
    """
        TournamentFileManager, manage the data acquisition from files
        :param  first_team: regex to obtain the first team name
                second_team: regex to obtain the second team name
                first_score: regex to obtain the first team score
                second_score: regex to obtain the second team score
    """
    def __init__(self):
        self.first_team = r'.+(?= \d+,)'
        self.second_team = r'(?<=, ).+(?= \d)'
        self.first_score = r'[0-9]+(?=, )'
        self.second_score = r'[0-9]+(?=\n)'
        self.export_filename = "output.txt"

    def extract_games_data(self):
        """ Return a list of iterables with the games,
            each iterable contains 2 dictionaries with the name and score of each team
            Eg:
                [[{'team': 'Crazy Ones', 'scored': '4'}, {'team': 'Rebels', 'scored': '3'}],..]
            :returns: List
        """
        matches_data = []
        reg_exp = fr'(?P<team>{self.first_team}|{self.second_team}) (?P<scored>[0-9]+)'
        for match_data in fileinput.input():
            matches_data.append([i.groupdict() for i in re.finditer(reg_exp, match_data) if i.groupdict()])
        return matches_data

    def extract_teams_data(self):
        """ Return a set of with the team names
            Eg:
            {'Crazy Ones', 'Fantastics', 'Rebels', 'Misfits', 'FC Super'}
            :returns: Set
        """
        teams = set()
        reg_exp = rf'(?P<team>{self.first_team}|{self.second_team})'
        for team in fileinput.input():
            teams.update([i for i in re.findall(reg_exp, team)])
        return teams

    def export(self, content):
        f = open(self.export_filename, "w")
        f.write(content)
        f.close()