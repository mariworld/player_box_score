import pprint


with open("roster.txt") as file:
    players = file.read().splitlines()

#print(players)
#we need a data structure to hold and organize the player info
#team -> has players -> each player has stats

#should take in player, minutes, assists, rebounds
def player_box_score(player=None, minutes=0, assists=0, rebounds=0, points=0):
    #how about a dictionary
    stats_dict = {
        "minutes": minutes,
        "assists": assists,
        "rebounds": rebounds,
        "points": points,
    }
    print(stats_dict)
    player_box = {player: stats_dict}
    pprint.pprint(player_box, width=1)
    return player_box

player_box_score("J.Tatum", 41, 8, 14, 25)

