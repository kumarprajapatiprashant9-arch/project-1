the source code is in the file source.py while the other file was me testing the code on my terms if you want to judge it judge on the level of code 
Terminal Bubble Shooter 🫧
A fully playable, terminal-based Bubble Shooter game written entirely in Python. This project features a turn-based grid system, automated score calculation, and flood-fill mechanics for popping matching bubbles, all while remaining strictly compliant with pre-defined unit tests.

Features
Terminal UI: Play the game directly in your command line with a clean, auto-refreshing interface.

Smart Match Detection: Uses a flood-fill algorithm to detect and pop adjacent bubbles of the same color (requires 3 or more).

Test-Driven: Core game logic (calculate_score, generate_level_grid, and format_grid) is decoupled from the game loop and passes standard assertion tests.

Dynamic Grid: Beautifully formatted grid output powered by the tabulate library.

Prerequisites
Before running the game, make sure you have Python installed on your machine. You will also need to install the tabulate library.

Bash
pip install tabulate
How to Play
Clone this repository or download the source.py file.

Open your terminal and navigate to the folder containing the file.

Run the game using Python:

Bash
python source.py
Controls
Aiming: When prompted, enter the column number (0-4) where you want to shoot your next bubble. The bubble will travel up the column until it hits the top or another bubble.

Quitting: Type q and press Enter to exit the game at any time.

Rules
Match 3 or more contiguous bubbles of the same color to pop them.

You earn 10 points for every bubble popped in a valid match.

The game ends when you clear the entire board (Win) or if a column becomes completely full (Game Over).

Testing
The core functions of this game were built to satisfy specific test conditions. If you are using a testing framework like pytest, you can safely run the file without triggering the interactive game loop:

Bash
pytest source.py
