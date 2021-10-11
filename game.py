from team import Team
from typing import List


class GameException(Exception):
    pass


class TeamGameData:
    """
        TeamGameData, contains the particular information of a team in a game.
        :param  game: List of
    """

    def __init__(self, team: Team, scored: int, *args, **kwargs):
        self.team = team
        self.score = scored


class Game:
    """
        Game, contains the information of the game, teams, winner, etc.
        :param  game: List of
    """

    def __init__(self, game_data: List[TeamGameData], *args, **kwargs):
        self.teams_game_data = game_data
        self.__validate_team_games_data()

    @property
    def winner(self) -> Team:
        """ Return the team instance of the winner or None if it's draw
        :returns: Obj (Team)
        """
        if self.teams_game_data[0].score > self.teams_game_data[1].score:
            return self.teams_game_data[0].team
        elif self.teams_game_data[0].score < self.teams_game_data[1].score:
            return self.teams_game_data[1].team

    @property
    def is_draw(self) -> bool:
        """ Returns true if it's a draw.
        :returns: Bool
        """
        return self.winner is None

    @property
    def teams(self) -> List[Team]:
        """ Returns a list with the team instances that play in the game
        :returns: List( Obj ( Team) )
        """
        return [i.team for i in self.teams_game_data]

    def __validate_team_games_data(self):
        if len(self.teams_game_data) != 2:
            breakpoint()
            raise GameException("Only 2 teams at a time can play a game.")
        if self.teams_game_data[0].team == self.teams_game_data[1].team:
            raise GameException("Same team playing against.")
