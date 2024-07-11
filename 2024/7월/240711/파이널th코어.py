def count(players):
    cnt = 0
    for player in players:
        cnt += players_list.count(player)
    return cnt

num_a, num_b, game_players = map(int, input().split())
team_a = input().split()
team_b = input().split()
players_list = input().split()

team_a_count = count(team_a)
team_b_count = count(team_b)

if team_a_count == team_b_count:
    print('TIE')
elif team_a_count > team_b_count:
    print('A')
else:
    print('B')
