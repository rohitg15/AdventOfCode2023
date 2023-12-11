from curses.ascii import isdigit
import re
import sys
from typing import List

# https://adventofcode.com/2023/day/3

def is_adj_symbol(lines: List[str], row: int, cbegin: int, cend: int ) -> bool:
    """
        returns True if there is an adjacent cell with a symbol
        returns False otherwise
    """
    m = len(lines)
    n = len(lines[row])

    # index to check all adjacent cells including diagonals
    dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for col in range(cbegin, cend):
        for dir in dirs:
            r = row + dir[0]
            c = col + dir[1]
            if r < 0 or r >= m or c < 0 or c >= n:
                continue

            ch = lines[r][c]
            if not isdigit(ch) and ch != '.':
                return True
    
    return False

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
    for i, line in enumerate(lines):
        
        # check every line for a match against integer patterns
        for digit_match in re.finditer(r'\d+', line):
            begin, end = digit_match.start(), digit_match.end()
            if is_adj_symbol(lines, i, begin, end):
                res += int(line[begin:end])
           
    print(res)

