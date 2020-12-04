from day.three.main import Move, get_trees_hit, tree_encounter


def test_tree_encounter():
    input_file = open("day/three/test_input.txt", "r")
    map_list = [l.strip() * 6 for l in input_file]
    move = Move(right=3, down=1)
    path_map = []
    trees_hit = []
    for i, j in tree_encounter(map_list, move):
        trees_hit.append(i)
        path_map.append(j)
    assert path_map == [
        "..##.........##.........##.........##.........##.........##.......",
        "#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
        ".#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
        "..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
        ".#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
        "..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....",
        ".#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
        ".#........#.#........X.#........#.#........#.#........#.#........#",
        "#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...",
        "#...##....##...##....##...#X....##...##....##...##....##...##....#",
        ".#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#",
    ]
    assert sum(trees_hit) == 7


def test_get_trees_hit():
    input_file = open("day/three/test_input.txt", "r")
    map_list = [l.strip() for l in input_file]
    move = Move(right=3, down=1)
    assert get_trees_hit(map_list, move) == 7
