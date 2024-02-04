from collections import defaultdict
import sys


# https://adventofcode.com/2023/day/4#part2
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print (f'Usage: {sys.argv[0]} input_file')
        sys.exit(-1)
    
    # parse each line from input file
    file_name = sys.argv[1]
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    num_lines = len(lines)
    total = 0
    copies = defaultdict(int, {i: 0 for i in range(num_lines + 1)})
    for i, line in enumerate(lines):
        index = i + 1
        # parse wins, current values for current card
        _, vals = line.split(':')
        winstr, curstr = vals.strip(' ').split('|')

        # remove empty strings from split
        wins, curs = list( filter(None, winstr.strip(' ').split(' ') ) ), list( filter( None, curstr.strip(' ').strip('\n').split(' ') ) )
        
        num_matches = sum((1 if cur in wins else 0 for cur in curs))
        cur = num_matches * (copies[index] + 1)
        for j in range(1, num_matches + 1):
            if index + j < num_lines:
                # next num_matches cards get 
                # 1 + copies[index] copies themselves
                # i.e 1 for current iteration + copies[index] for
                # prior copies of this card
                copies[index + j] += (copies[index] + 1)
        total += copies[index] + 1

    print (total)