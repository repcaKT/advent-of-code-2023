import re
from collections import defaultdict
from data_tools import data_reader, multiply_list

# not too proud of this one, but had a lot of fun :D 

input_data = data_reader("puzzle_input.txt")
parts_numbers = []
gears = defaultdict(list)
for schema_idx, single_schematic in enumerate(input_data):
    for number_match in re.finditer(r"\d+", single_schematic):        
        #check left
        if number_match.start() != 0 and bool(re.match(r"[^0-9.\n]", single_schematic[number_match.start()-1])):
            parts_numbers.append(int(number_match.group()))
            found_symbol = re.match(r"[^0-9.\n]", single_schematic[number_match.start()-1])
            if(found_symbol.group() == "*"):
                gears[f"{schema_idx}:{number_match.start()-1}"].append(int(number_match.group()))
            continue
         #check right 
        if number_match.end() != len(single_schematic) and bool(re.match(r"[^0-9.\n]", single_schematic[number_match.end()])):
            parts_numbers.append(int(number_match.group()))
            found_symbol = re.match(r"[^0-9.\n]", single_schematic[number_match.end()])
            if(found_symbol.group() == "*"):
                gears[f"{schema_idx}:{number_match.end()}"].append(int(number_match.group()))
            continue
        #check up
        if schema_idx != 0 and bool(re.search(r"[^0-9.\n]", input_data[schema_idx-1][number_match.start():number_match.end()])): 
            parts_numbers.append(int(number_match.group()))
            found_symbol = re.search(r"[^0-9.\n]", input_data[schema_idx-1][number_match.start():number_match.end()])
            if(found_symbol.group() == "*"):
                gears[f"{schema_idx-1}:{number_match.start()+found_symbol.start()}"].append(int(number_match.group()))
            continue
        #check down
        if schema_idx != len(input_data)-1 and bool(re.search(r"[^0-9.\n]", input_data[schema_idx+1][number_match.start():number_match.end()])): 
            parts_numbers.append(int(number_match.group()))
            found_symbol = re.search(r"[^0-9.\n]", input_data[schema_idx+1][number_match.start():number_match.end()])
            if(found_symbol.group() == "*"):
                gears[f"{schema_idx+1}:{number_match.start()+found_symbol.start()}"].append(int(number_match.group()))
            continue
        #check left up
        if number_match.start() != 0 and schema_idx != 0 and bool(re.match(r"[^0-9.\n]", input_data[schema_idx-1][number_match.start()-1])):
            parts_numbers.append(int(number_match.group()))
            found_symbol = re.match(r"[^0-9.\n]", input_data[schema_idx-1][number_match.start()-1])
            if(found_symbol.group() == "*"):
                gears[f"{schema_idx-1}:{number_match.start()-1}"].append(int(number_match.group()))
            continue
         #check right up
        if number_match.end() != len(single_schematic) and schema_idx != 0 and bool(re.match(r"[^0-9.\n]", input_data[schema_idx-1][number_match.end()])):
            parts_numbers.append(int(number_match.group()))
            found_symbol = re.match(r"[^0-9.\n]", input_data[schema_idx-1][number_match.end()])
            if(found_symbol.group() == "*"):
                gears[f"{schema_idx-1}:{number_match.end()}"].append(int(number_match.group()))
            continue
        #check left down
        if number_match.start() != 0 and schema_idx != len(input_data)-1 and bool(re.match(r"[^0-9.\n]", input_data[schema_idx+1][number_match.start()-1])):
            parts_numbers.append(int(number_match.group()))
            found_symbol = re.match(r"[^0-9.\n]", input_data[schema_idx+1][number_match.start()-1])
            if(found_symbol.group() == "*"):
                gears[f"{schema_idx+1}:{number_match.start()-1}"].append(int(number_match.group()))
            continue
        #check right down
        if number_match.end() != len(single_schematic) and schema_idx != len(input_data)-1 and bool(re.match(r"[^0-9.\n]", input_data[schema_idx+1][number_match.end()])):
            parts_numbers.append(int(number_match.group()))
            found_symbol = re.match(r"[^0-9.\n]", input_data[schema_idx+1][number_match.end()])
            if(found_symbol.group() == "*"):
                gears[f"{schema_idx+1}:{number_match.end()}"].append(int(number_match.group()))
            continue

print(f"The sum of all of the part numbers: {sum(parts_numbers)}")
print(f"the sum of all of the gear ratios: {sum([multiply_list(gear) for gear in gears.values() if len(gear) is 2])}")
