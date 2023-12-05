import re
from collections import defaultdict

#part 1
with open("puzzle_input.txt") as f:
    print("points are they worth in total: " + str(sum([round(pow(2, len(set(ticket[2].split()).intersection(set(ticket[1].split())))-1)) for ticket in [re.split(":|\|", ticket) for ticket in f]])))

#part 2
with open("puzzle_input.txt") as f:
    scratches = defaultdict(list)
    for win_len in enumerate([len(set(ticket[2].split()).intersection(set(ticket[1].split()))) for ticket in [re.split(":|\|", ticket) for ticket in f]]):
        scratches[win_len[0]].append(1)
        for tix_ammount in range(win_len[1]):
            for _ in scratches[win_len[0]]:
                scratches[tix_ammount+1+win_len[0]].append(1)
    print("total scratchcards ammount: "+str(sum([len(scratch) for scratch in scratches.values()])))