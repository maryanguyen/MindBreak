# **MindBreak**

A Python command-line game recommendation tool that helps you pick a game based on your current mood, preferred genre, platform, and how much time you have to play.

## Description

Can't decide what to play? MindBreak asks you four simple questions and instantly recommends a game matched to your answers. With 192 possible combinations, there's always something for you.

## Features

- **Recommendations** based on mood, genre, platform, and time
- **Input validation** — rejects invalid entries and re-prompts until a valid option is given
- **Case-insensitive** — type `relaxed`, `RELAXED`, or `Relaxed`, it all works
- **Loops until done** — ask for as many recommendations as you want
- **Error handling** — handles missing files and incorrect input
- **Portable** — runs from any computer without changing file paths

## How to Run

1. **Clone the repository**
   ```
   git clone https://github.com/your-username/mindbreak.git
   cd mindbreak
   ```
3. **Make sure _both_ files are in the _same_ folder**
   ```
   FinalProject_MaryNguyen.py
   games.txt
   ```
   
5. **Run the program**
   ```
   python FinalProject_MaryNguyen.py
   ```
   
* *No external libraries needed — uses Python's built-in `os` module only.* *

## How It Works
```
Welcome to MindBreak!
We'll help you choose a game to save you time!

Mood (Relaxed, Stressed, Energetic, Bored): relaxed
Genre (Puzzle, Adventure, Action, Simulation): puzzle
Platform (PC, Console, Mobile): pc
Time (5-10, 15-30, 30-60, 1+): 5-10

🎮 Recommended Game: Minesweeper

Would you like another recommendation? (yes/no): no

Thank you for using MindBreak!
```

## Input Options

| Category | Options |
|----------|---------|
| **Mood** | Relaxed, Stressed, Energetic, Bored |
| **Genre** | Puzzle, Adventure, Action, Simulation |
| **Platform** | PC, Console, Mobile |
| **Time** | 5-10, 15-30, 30-60, 1+ |


## File Structure

mindbreak/
```
├── FinalProject_MaryNguyen.py   # Main program
├── games.txt                    # Game database (192 combinations)
└── README.md                    # You're reading this!
```

### games.txt Format

Each line follows this format:
```
Mood,Genre,Platform,Time,Game Name
```

Example:
```
Relaxed,Puzzle,Mobile,5-10,Candy Crush
Energetic,Action,Console,30-60,Rocket League
Bored,Adventure,PC,1+,Stardew Valley
```

## Requirements

- Python 3.x
- No additional packages required
