from dataclasses import dataclass, field

from data_tools import data_reader, multiply_list

@dataclass
class CubeGame:
    game_number: int
    game_sets: list[str]
    min_no_of_cubes: dict = field(default_factory=lambda: {
        "red": 1,
        "green": 1,
        "blue": 1
    })

    @staticmethod
    def split_set_string(set_string: str) -> list[tuple]:
        return [tuple(cube.strip().split(" ")) for cube in set_string.split(",")]
    
    def set_no_cubes(self):
        for game_set in self.game_sets:
            cubes = self.split_set_string(game_set)
            for cube_count, cube_color in cubes:
                if int(cube_count)>self.min_no_of_cubes[cube_color]:
                    self.min_no_of_cubes[cube_color] = int(cube_count)
    
    def get_game_power(self):
        self.set_no_cubes()
        return multiply_list(self.min_no_of_cubes.values())

def split_to_cube_games(single_input: str)->CubeGame:
    game_name, game_sets = single_input.split(":", 1)
    game_number = int(game_name.split(" ")[-1])
    sets_list = game_sets.split(";")
    return CubeGame(game_number=game_number, game_sets=sets_list)

def main():
    cube_games_list = data_reader("puzzle_input.txt")

    result = sum([cube_game_obj.get_game_power() for cube_game_obj in [split_to_cube_games(cube_game) for cube_game in cube_games_list]])
    print(f"Sum of all possible game powers equals to: {result}")

if __name__ == "__main__":
    main()