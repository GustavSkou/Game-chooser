import random
ran = random.uniform(0, 5)
to_play_size = 0

# Creating list of lists
    # hvert ting i listen i listen er et item startene fra 0 op til 3, dette bruger vi til
    # at kunne kategorisere item 0 med de resterne items
games = [["Escape from tarkov", "multiplayer", "pvpve", "long"],
    ["League of legends", "multiplayer", "pvp", "short"],
    ["Rocket league", "multiplayer", "pvp", "short"],
    ["Minecraft", "multiplayer", "pve", "long"],
    ["Shatterline" "multiplayer", "pve", "medium"],
    ["Among us", "multiplayer", "pvp", "short"],
    ["Rainbow six siege", "multiplayer", "pvp", "medium"],
    ["Phasmophobia", "multiplayer", "pve", "medium"],
    ["Euto truck simulator 2", "multiplayer", "driving"]]

# input type
print("Hvilken type spil vil du spille")
type = input()

# input length
print("Hvor lang tid vil du spille")
length = input()

to_play = []                                            # create an emtpy list for the games

for item in games:                                      # create list of games
    if item[2] == type and item[3] == length:
        to_play.append(item[0])                         # list over corresponding games
to_play_size = len(to_play)                             # check how many corresponding games there is

print(to_play)
print(to_play_size)

#if to_play_size == 2:
#  ran = random.uniform(0, to_play_size-1)
# print(to_play[ran] + type + length)




'''
    elif item[2] == type and item[3] != length :
        print(type + " " + item[3] + " " + item[0])
'''
'''
while answer != "quit":
    answer = input("choose random game (y/n) ")
    value = random.uniform(0, 5)
    if answer == "y":
        print(games[int(value)])
    elif answer == "n":
        answer = input("choose random game (y/n) ")
'''
'''
for y in range(100):
    print(int(value), end=" ")
    value = random.uniform(1, 10)
'''