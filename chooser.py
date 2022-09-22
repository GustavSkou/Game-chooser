import random
random.seed()

short = 1
medium = 2
long = 3
forever = 4
type_answer = 1
length_answer = 1

# Creating list of lists
    # each row's item[0] is being represented by 3 categories
games = [["Escape from tarkov", "multiplayer", "pvpve", long],
    ["League of legends", "multiplayer", "pvp", short],
    ["Rocket league", "multiplayer", "pvp", short],
    ["Minecraft", "multiplayer", "pve", forever],
    ["Shatterline" "multiplayer", "pve", medium],
    ["Among us", "multiplayer", "pvp", short],
    ["Rainbow six siege", "multiplayer", "pvp", medium],
    ["Phasmophobia", "multiplayer", "pve", medium],
    ["Euro truck simulator 2", "multiplayer", "driving", long],
    ["CSGO", "multiplayer", "pvp", medium],
    ["Cities: Skylines", "Singleplayer", "pve", forever],
    ["Freedom Fighters", "Singleplayer", "pve", medium],
    ["Hunt: Showdown", "Multiplayer", "pvpve", medium],
    ["Rust", "multiplayer", "pvpve", long],
    ["Arma 3", "multiplayer", "pvp", long],
    ["Castle Story", "singleplayer", "pve", medium],
    ["Apex legends", "multiplayer", "pvp", medium],
    ["PUBG", "multiplayer", "pvp", medium],
    ["Terraria", "singleplayer", "pve", long],
    ["Subnautica", "singleplayer", "pve", medium],
    ["Stormworks", "singleplayer", "pve", long],
    ["Worms", "multiplayer", "pvp", medium],
    ["War thunder", "multiplayer", "pvp", medium],
    ["No man's sky", "singleplayer", "pve", long]]

game_types = ["pvp", "pve", "pvpve", "driving"]         # List of the type of games, item(2) in games

# input type
print("What kind of game would you like to play (pvp, pve, pvpve, driving)")
while type_answer == 1:
    type = input()
    if type in game_types:
        type_answer = 0
    else:
        print("try again")

# input length
print("For how long do you want to play (short, medium, long, forever)")
while length_answer == 1:
    length = input()
    if length == "short":
        length = 1
        length_answer = 0
    elif length == "medium":
        length = 2
        length_answer = 0
    elif length == "long":
        length = 3
        length_answer = 0
    elif length == "forever":
        length = 4
        length_answerx = 0
    else:
        print("try again")

to_play = []                                            # Create an emtpy list for the games to play
for item in games:
    if item[2] == type and item[3] == length:
        to_play.append(item[0])                         # Add games to the to_play list
to_play_size = len(to_play)                             # Check how many corresponding games there is

if to_play_size >= 2:                                   # If the list contains more than 1 game
    ran = random.uniform(0, to_play_size)               # Gets random number to the size of how many games were found
    print(to_play[int(ran)])                            # Uses random number to print
elif to_play_size == 0:                                 # If there wasn't any corresponding games
    for item in games:
        if item[2] == type and item[3] == length-1 or item[2] == type and item[3] == length+1:  # Check if theres is corresponding games to the type and the length +- 1
            to_play.append(item[0])
    to_play_size = len(to_play)
    ran = random.uniform(0, to_play_size)               # Gets random number to the size of how many games were found
    print(to_play[int(ran)])                            # Uses random number to print
else:                                                   # If the list only contains 1 game
    print(to_play)