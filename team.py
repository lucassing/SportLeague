class Team:
    """
        Tournament object
        :param  name: the team name
                foundation: the foundation's year of the team
        """
    def __init__(self, name, *args, **kwargs):
        self.team_name = name
        self.foundation = kwargs.get('foundation')

    def __str__(self):
        return str(self.team_name)
