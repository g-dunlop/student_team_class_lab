

class Team:
    def __init__(self, team_name, team_players, team_coach):
        self.name = team_name
        self.players = team_players
        self.coach = team_coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)
    
    def has_player(self, player):
        if player in self.players:
            return True
        else:
            return False

    def play_game(self, match):
        if match == True:
            self.points += 3
        else:
            return self.points

