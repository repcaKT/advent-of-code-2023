from dataclasses import dataclass

from data_tools import data_reader


CUBE_SET = {
    "red": 12,
    "green": 13,
    "blue": 14
}

@dataclass
class CubeGame:
    game_number: int
    game_sets: list[str]

def split_to_cube_games(single_input: str)->CubeGame:
    game_name, game_sets = single_input.split(":", 1)
    game_number = int(game_name.split(" ")[-1])
    sets_list = game_sets.split(";")
    return CubeGame(game_number=game_number, game_sets=sets_list)


def split_set_string(set_string: str) -> list[tuple]:
    return [tuple(cube.strip().split(" ")) for cube in set_string.split(",")]

def is_game_possible(game: CubeGame) -> bool:
    for game_set in game.game_sets:
        cubes = split_set_string(game_set)
        if any(int(cube_count) > CUBE_SET[cube_color] for cube_count, cube_color in cubes):
            return False
    return True


def main():
    # cube_games_list = data_reader("puzzle_input.txt")
    cube_games_list = data_reader("C://Users//Tatahah//Projects//advent-of-code-2023//day_2//puzzle_input.txt")

    result = sum([cube_game_obj.game_number if is_game_possible(cube_game_obj) else 0 for cube_game_obj in [split_to_cube_games(cube_game) for cube_game in cube_games_list]])
    print(f"Sum of all possible game numbers equals to: {result}")

if __name__ == "__main__":
    main()