import re
from data_tools import data_reader


DIGIT_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def number_finder(messed_calibration:str):
    pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))') # here we are looking for all digits in the string

    digits = [match.group(1) for match in pattern.finditer(messed_calibration)]
    first_digit = digits[0] if digits[0].isdigit() else DIGIT_DICT[digits[0]]
    second_digit = digits[-1] if digits[-1].isdigit() else DIGIT_DICT[digits[-1]]
    return (int(first_digit+second_digit))

def main():
    calibration_list = data_reader("puzzle_input.txt")
    result = sum([number_finder(messed_calibration) for messed_calibration in calibration_list])
    print(f"Sum of all of the calibration values equals to: {result}")

if __name__ == "__main__":
    main()
