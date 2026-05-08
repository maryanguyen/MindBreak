import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# load file
def load_games(filename):
    games = []

    # open file and read each line
    with open(filename, "r") as file:    
        for line in file:
            # remove newline and split by commas
            parts = line.strip().split(",")
                
            # create dictionary for each game
            game = {
                "mood": parts[0],
                "genre": parts[1],
                "platform": parts[2],
                "time": parts[3],
                "name": parts[4]
                }
            # adds game to list
            games.append(game)

    # return list of games
    return games

# collect preferences and checks input against valid options
def collect_choices():
    # user must select from the valid options only
    valid_mood = ["RELAXED", "STRESSED", "ENERGETIC", "BORED"]
    valid_genre = ["PUZZLE", "ADVENTURE", "ACTION", "SIMULATION"]
    valid_platform = ["PC", "CONSOLE", "MOBILE"]
    valid_time = ["5-10", "15-30", "30-60", "1+"]
    
    while True:
        mood = input("😌 Mood (Relaxed, Stressed, Energetic, Bored): ").strip().upper()
        if mood in valid_mood:
            break
        print("Invalid mood. Please choose from: Relaxed, Stressed, Energetic, or Bored")
    while True:
        genre = input("🎲 Genre (Puzzle, Adventure, Action, Simulation): ").strip().upper()
        if genre in valid_genre:
            break
        print("Invalid genre. Please choose from: Puzzle, Adventure, Action, or Simulation")
    while True:
        platform = input("🖥️ Platform (PC, Console, Mobile): ").strip().upper()
        if platform in valid_platform:
            break
        print("Invalid platform. Please choose from: PC, Console, or Mobile")
    while True:
        time = input("⏱️ Time (5-10, 15-30, 30-60, 1+): ").strip().upper()
        if time in valid_time:
            break
        print("Invalid time. Please choose from: 5-10, 15-30, 30-60, or 1+")

    return mood, genre, platform, time

# compares choices to game list and returns matching game name
def find_game(games, mood, genre, platform, time):
    # loop through games list
    for game in games:
        if (game["mood"].upper() == mood and
            game["genre"].upper() == genre and
            game["platform"].upper() == platform and
            game["time"].upper() == time):
            return game["name"]
    # if no match found
    return None

# welcome user to begin asking for input
def main():
    print("Welcome to MindBreak!")
    print("Let us choose your game to save you time!\n")

    # load games from file
    games = load_games("games.txt")

    # loop to run the program multiple times
    while True:
        mood, genre, platform, time = collect_choices()

        # find game recommendation
        result = find_game(games, mood, genre, platform, time)

        # output result
        if result:
            print("\n🎮 Recommended Game:", result)
        else:
            print("\nSorry, no exact match was found.")

        # ask if user wants to continue
        while True:
            again = input("\nWould you like another recommendation? (yes/y/no/n): ").strip().lower()
            if again in ["yes", "y", "no", "n"]:
                break
            print("Please enter yes/no or y/n.")

        if again in ["no", "n"]:
            print("\nThank you for using MindBreak!")
            break
# run program
main()
