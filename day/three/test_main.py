from day.three.main import Move, get_trees_hit

test_input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_get_trees_hit():
    move = Move(right=3, down=1)
    assert get_trees_hit(test_input, move) == 7
