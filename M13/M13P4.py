def load_players(filename):
    players = {}
    try:
        f = open(filename, "r")
    except:
        print("Could not open file.")
        return players
    for line in f:
        line = line.strip()
        if line == "":
            continue
        parts = line.split()
        if len(parts) >= 2:
            name = parts[0]
            avg = float(parts[1])
            players[name] = avg
    f.close()
    return players

def main():
    filename = input("Enter player file name (e.g. players.txt): ")
    players = load_players(filename)
    if len(players) == 0:
        return

    name = input("Enter player name to look up (or DONE to quit): ")
    while name != "DONE":
        if name in players:
            print(name, players[name])
        else:
            print("Player not found")
        name = input("Enter player name to look up (or DONE to quit): ")

main()
