from source import calculate_score, generate_level_grid, format_grid

def test_calculate_score():
    assert calculate_score(1) == 0
    assert calculate_score(2) == 0
    assert calculate_score(3) == 30
    assert calculate_score(5) == 50

def test_generate_level_grid():
    grid = generate_level_grid(3, 4)
    assert len(grid) == 3
    assert len(grid[0]) == 4

    assert generate_level_grid(0, 5) == []
    assert generate_level_grid(5, 0) == []

def test_format_grid():
    assert format_grid([]) == "Empty"

    grid = [["Ruby", "Sapphire"], ["Emerald", "Ruby"]]
    formatted = format_grid(grid)

    # tabulate prints the grid with + and - characters
    assert "+" in formatted
    assert "Ruby" in formatted
    assert "Emerald" in formatted