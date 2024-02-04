import re
import sys
from typing import List, Tuple

# https://adventofcode.com/2023/day/3#part2

def is_adj_gear(lines: List[str], row: int, cbegin: int, cend: int) -> Tuple[int, int]:
    """
        returns True if there is an adjacent cell with a gear
        returns False otherwise
    """
    m = len(lines)
    n = len(lines[row])

    # index to check all adjacent cells including diagonals
    dirs = (
        (-1, -1),
        (-1, 0), 
        (-1, 1), 
        (0, -1), 
        (0, 1), 
        (1, -1), 
        (1, 0), 
        (1, 1)
    )
    for col in range(cbegin, cend):
        for dir in dirs:
            r = row + dir[0]
            c = col + dir[1]
            if r < 0 or r >= m or c < 0 or c >= n:
                continue

            ch = lines[r][c]
            if ch == '*':
                return (r, c)
    
    return (None, None)



# https://adventofcode.com/2023/day/3
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print (f'Usage: {sys.argv[0]} input_file')
        sys.exit(-1)
    
    # parse each line from input file
    file_name = sys.argv[1]
    lines = []
    with open(file_name, 'r') as file:
        lines = [line.strip('\n') for line in file.readlines()]

    res = 0
    gears = {}
    for i, line in enumerate(lines):
        # check every line for a match against integer patterns
        for digit_match in re.finditer(r'\d+', line):
            begin, end = digit_match.start(), digit_match.end()
            r, c = is_adj_gear(lines, i, begin, end)
            
            # add numbers to gears, keyed by gear position
            if r is not None and c is not None:
                key = f'{r}#{c}'
                if gears.get(key) is None:
                    gears[key] = []
                gears[key].append(int(line[begin:end]))
    
    # count only if there are 2 numbers adjacent to a gear
    res = sum(gear_val[0] * gear_val[1] for gear_val in gears.values() if len(gear_val) == 2)
    print(res)

