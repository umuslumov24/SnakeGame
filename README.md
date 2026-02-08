# 🐍 **Traditional Snake Game (Python Turtle)**

A simple and classic Snake Game built using Python’s turtle module.
This project includes features such as movement control, collision detection, food generation, score tracking, and a persistent high score system.<br><br>

## ⚙️ **Features**

Smooth snake movement

Food appears in random positions

Snake grows after eating

Wall collision detection

Self-collision detection

Persistent High Score saved in a text file

Clean,simple and structured OOP design (Snake, Food, Scoreboard)<br><br>

## 📂 **Project Structure**


├── main.py

├── Snakes.py

├── Food.py

├── SB.py

├── Highest_Score.txt

└── README.md<br><br>

--- main.py ---

Handles the game screen, user input, and game loop.

--- Snakes.py ---

Defines the Snake class: movement, growing, resetting, and self-collision.

--- Food.py ---

Creates food objects and relocates them randomly on the screen.

--- SB.py ---

Scoreboard class: tracks current score, saves high score.

--- Highest_Score.txt ---

Stores the highest score across game sessions.<br><br>

## ▶️ **How to Run** 

1. Make sure you have Python 3 installed.

2. Clone the repository:
git clone https://github.com/yourusername/your-repo-name.git

3. Open the project folder:
cd your-repo-name

4. Run the game:
python main.py<br><br>

## ⌨️ **Controls**

↑	Move Up

↓	Move Down

←	Move Left

→	Move Right

Snake cannot directly turn backward.<br><br>

## 🏆 **High Score System**

High score is stored in Highest_Score.txt

The file is automatically created if it does not exist

When the snake hits a wall or itself, the game resets but the high score persists<br><br>

## 📈 **Future Improvements**

Add sound effects

Add a game-over animation

Add custom skins or colors<br><br>

## 📜 **License**

This project is open-source. Feel free to modify and improve it!
