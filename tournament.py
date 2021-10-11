from game import Game
from typing import List


class TournamentException(Exception):
    pass


class Tournament:
    """
    Tournament object
    :param  teams: set of Team instance
            year: int year of the Tournament
            game: list of game instance
    """

    def __init__(self,
                 teams=None,
                 year=0,
                 *args,
                 **kwargs):
        self.teams = teams
        self.year = year
        self.games = []

    def add_game(self, game: Game):
        """ Append a new game instance to the list of games of the tournament
        :param game: Game instance
        :returns: None
        """
        self.games.append(game)

    def add_bulk_game(self, games: List[Game]):
        """ Append an iterable of game instances to the list of games of the tournament
        :param games: List of game
        :returns: None
        """
        for i in games:
            self.add_game(i)

    def stats(self):
        """ Return the sorted list of tuples with the team and it's stats.
            :returns: list of tuple with team and stat
            """
        stats = dict.fromkeys(self.teams, 0)
        for game in self.games:
            if game.winner is None:
                for team in game.teams:
                    stats[team] += 1
            else:
                stats[game.winner] += 3
        return sorted(stats.items(), key=lambda x: x[1], reverse=True)

    def _calculate_position(self):
        stats = self.stats()
        table = []
        if stats:
            pivot = stats[0]
            position = 1
            table.append({'position': position, 'team': pivot[0], 'point': pivot[1]})
            for index in range(1, len(stats)):
                if stats[index][1] != pivot[1]:
                    position = index + 1

                stat = {'position': position,
                        'team': stats[index][0],
                        'point': stats[index][1]}
                pivot = stats[index]
                table.append(stat)
        else:
            raise TournamentException("Tournament has no games added")
        return table

    def __str__(self):
        st = ''
        for stat in self._calculate_position():
            st += f"{stat['position']} {stat['team'].team_name} {stat['point']} \n"
        return st
