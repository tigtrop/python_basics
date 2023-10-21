class Team_score:
    def __init__(self, win_games, draw_games, lose_games, goals, misses):
        self.win_games = win_games
        self.draw_games = draw_games
        self.lose_games = lose_games
        self.goals = goals
        self.misses = misses

    def match_score(self):
        return self.goals, self.misses

    def score(self):
        return (self.win_games * 3) + self.draw_games

    def goals_diff(self):
        return self.goals - self.misses

class Team_score_add(Team_score):
    def __init__(self, win_games, lose_games, draw_games, goals, misses):
        super().__init__(win_games, lose_games, draw_games, goals, misses)
    def all_games(self):
        return self.win_games + self.lose_games + self.draw_games

momba_team = Team_score(10,5,3,13,8)

print(momba_team.match_score())
print((momba_team.score()))
print(momba_team.goals_diff())

gomba_team = Team_score_add(8, 6, 2, 8, 6)

if __name__ == '__main__':

    print(gomba_team.all_games())
    print(gomba_team.match_score())
    print((gomba_team.score()))
    print(gomba_team.goals_diff())
