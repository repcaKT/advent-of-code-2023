import re
from data_tools import data_reader


def number_finder(messed_calibration:str):
    digits = re.findall(r"\d", messed_calibration) # here we are looking for all digits in the string
    return (int(digits[0]+digits[-1])) # here we are concat two digits (in form of strings) and converting it to int

def main():
    calibration_list = data_reader("puzzle_input.txt")
    result = sum([number_finder(messed_calibration) for messed_calibration in calibration_list])
    print(f"Sum of all of the calibration values equals to: {result}")

if __name__ == "__main__":
    main()
