import random

# Creating list of lists
    # each row's item[0] is being represented by 3 categories
games = [["Escape from tarkov", "multiplayer", "pvpve", "long"],
    ["League of legends", "multiplayer", "pvp", "medium"],
    ["Rocket league", "multiplayer", "pvp", "short"],
    ["Minecraft", "multiplayer", "pve", "long"],
    ["Shatterline" "multiplayer", "pve", "medium"],
    ["Among us", "multiplayer", "pvp", "short"],
    ["Rainbow six siege", "multiplayer", "pvp", "medium"],
    ["Phasmophobia", "multiplayer", "pve", "medium"],
    ["Euro truck simulator 2", "multiplayer", "driving"]]

# input type
print("Hvilken type spil vil du spille")
type = input()

# input length
print("Hvor lang tid vil du spille")
length = input()

to_play = []                                            # create an emtpy list for the games to play
for item in games:
    if item[2] == type and item[3] == length:
        to_play.append(item[0])                         # Add games to the to_play list
to_play_size = len(to_play)                             # check how many corresponding games there is

if to_play_size >= 2:                                   # If the list contains more than 1 game
    ran = random.uniform(0, to_play_size-1)
    print(to_play[int(ran)])