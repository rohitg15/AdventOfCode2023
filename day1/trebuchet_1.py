from curses.ascii import isdigit
import sys

# https://adventofcode.com/2023/day/1

def get_digits(line: str) -> int:
    digits = ''.join(ch if isdigit(ch) else '' for ch in line)
    return int(digits[0] + digits[-1])

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print (f'Usage: {sys.argv[0]} input_file')
        sys.exit(-1)
    
    file_name = sys.argv[1]
    lines = []
    with open(file_name, 'r') as file:
        lines = file.readlines()

    s = sum(get_digits(line.strip('\n')) for line in lines)
    print (s)

