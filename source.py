import random
import os
from tabulate import tabulate

def calculate_score(bubbles_popped):
    if bubbles_popped >= 3:
        return bubbles_popped * 10
    return 0

def generate_level_grid(rows, cols):
    if rows <= 0 or cols <= 0:
        return []
    colors = ["Ruby", "Sapphire", "Emerald", "Topaz", "Amethyst"]
    return [[random.choice(colors) for _ in range(cols)] for _ in range(rows)]

def format_grid(grid):
    if not grid:
        return "Empty"
    return tabulate(grid, tablefmt="grid")

class BubbleShooterGame:
    def __init__(self, rows=8, cols=5):
        self.rows = rows
        self.cols = cols
        self.score = 0
        self.colors = ["Ruby", "Sapphire", "Emerald", "Topaz", "Amethyst"]
        top_grid = generate_level_grid(3, cols)
        empty_rows = [["" for _ in range(cols)] for _ in range(rows - 3)]
        self.grid = top_grid + empty_rows
        self.current_bubble = random.choice(self.colors)

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"==========================================")
        print(f"  Score: {self.score}  |  Next Bubble: {self.current_bubble}")
        print(f"==========================================")
        print(format_grid(self.grid))
        col_headers = "   ".join([f"({i})" for i in range(self.cols)])
        print("Columns:  " + col_headers + "\n")

    def shoot(self, col):
        target_row = -1
        for r in range(self.rows - 1, -1, -1):
            if self.grid[r][col] == "":
                target_row = r
            else:
                break
        
        if target_row == -1:
            return False

        self.grid[target_row][col] = self.current_bubble
        self.resolve_matches(target_row, col)
        self.current_bubble = random.choice(self.colors)
        return True

    def resolve_matches(self, r, c):
        target_color = self.grid[r][c]
        if not target_color: 
            return
        
        visited = set()
        stack = [(r, c)]
        match_group = []

        while stack:
            curr_r, curr_c = stack.pop()
            if (curr_r, curr_c) not in visited:
                visited.add((curr_r, curr_c))
                if self.grid[curr_r][curr_c] == target_color:
                    match_group.append((curr_r, curr_c))
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            stack.append((nr, nc))
        
        if len(match_group) >= 3:
            for mr, mc in match_group:
                self.grid[mr][mc] = ""
            self.score += calculate_score(len(match_group))

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] != "":
                    return False
        return True

def main():
    game = BubbleShooterGame()
    while True:
        game.display()
        if game.check_win():
            print("🎉 YOU CLEARED THE BOARD! YOU WIN! 🎉")
            break
        try:
            player_input = input(f"Enter column number (0-{game.cols-1}) to shoot, or 'q' to quit: ")
            if player_input.lower() == 'q':
                print("Thanks for playing!")
                break
            col = int(player_input)
            if 0 <= col < game.cols:
                success = game.shoot(col)
                if not success:
                    game.display()
                    print("Game Over! That column is completely full.")
                    break
            else:
                input("Invalid column! Press Enter to try again...")
        except ValueError:
            input("Please enter a valid number. Press Enter to try again...")

if __name__ == "__main__":
    main()