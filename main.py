from filemanager import TournamentFileManager
from team import Team
from game import Game, TeamGameData
from tournament import Tournament
import fileinput


class TournamentFactory:

    def __init__(self, teams, games):

        # Create Teams
        self.teams_instances = dict(map(lambda x: (x, Team(x)), teams))

        # Create Tournament
        self.tournament_instance = Tournament(teams=list(self.teams_instances.values()))

        # Create Game instances for the tournament
        self.games_instances = []

        for game in games:
            team_game_data_instances = []
            for team_data in game:
                # Creates a list with TeamGameData, 'team' replace with team instance
                team_game_data_instances.append(TeamGameData(**{**team_data,
                                                                'team': self.teams_instances[team_data['team']]}))
            self.tournament_instance.add_game(Game(team_game_data_instances))


if __name__ == '__main__':
    # Extraction of data from file
    tournament_file_manager = TournamentFileManager()
    teams_data = tournament_file_manager.extract_teams_data()
    games_data = tournament_file_manager.extract_games_data()

    tf = TournamentFactory(teams_data, games_data)

    tournament_file_manager.export(str(tf.tournament_instance))
