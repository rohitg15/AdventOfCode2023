from curses.ascii import isdigit
import sys

# https://adventofcode.com/2023/day/1#part2

def get_first_digit(line: str, l2r: bool) -> chr:

    digit_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    l = len(line)
    i = 0 if l2r else l - 1
    res = []
    while True:
        # iterate from l2r or r2l as indicated
        if l2r and i >= l:
            break
        if not l2r and i < 0:
            break

        # examine strings of length 3, 4, 5 against digit_map
        # since those are the sizes of the values in the digit_map. 
        match_set = (line[i: i+3], line[i: i+4], line[i:i+5]) if l2r else (line[i: i-3: -1], line[i: i-4: -1], line[i:i-5:-1])
        is_replaced = False
        for j, pkey in enumerate(match_set):
            key = pkey if l2r else pkey[::-1]
            if digit_map.get(key) is not None:
                # if a match is found, replace by digit in the result set
                # and update iterator by corresponding length
                res.append(digit_map[key])
                i = i + j + 3 if l2r else i - j - 3
                is_replaced = True
                break
        
        # if no match from match_set, then add current character 
        # to the result set and move to next character
        if not is_replaced:
            res.append(line[i])
            i = i + 1 if l2r else i - 1
    
    return next((ch for ch in ''.join(res) if isdigit(ch)), '')


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print (f'Usage: {sys.argv[0]} input_file')
        sys.exit(-1)
    
    # parse input lines from file
    file_name = sys.argv[1]
    lines = []
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # examine from l2r and r2l to handle the following
    # eg: oneight must resolve to 18
    get_digits = lambda line : int(get_first_digit(line, l2r=True) + get_first_digit(line, l2r=False))
    
    s = sum(get_digits(line.strip('\n'))  for line in lines)
    print (s)

