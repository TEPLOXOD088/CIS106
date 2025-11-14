def print_players(players):
    print("Player\tAverage")
    print("------\t-------")
    for name, avg in players.items():
        print(name + "\t" + str(avg))

def main():
    filename = input("Enter player file name (e.g. players.txt): ")
    players = {}
    try:
        f = open(filename, "r")
    except:
        print("Could not open file.")
        return

    for line in f:
        line = line.strip()
        if line == "":
            continue
        parts = line.split()
        if len(parts) >= 2:
            name = parts[0]
            avg_str = parts[1]
            avg = float(avg_str)
            players[name] = avg
    f.close()

    print_players(players)

main()
