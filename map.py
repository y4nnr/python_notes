list_teams = ['nice', 'paris', 'porto', 'bordeaux', 'monaco']

def find_team_p(team):
    if team[0] == 'p':
        return team

map_team = map(find_team_p, list_teams)

print(map_team)

for i in map_team:
    print(i)