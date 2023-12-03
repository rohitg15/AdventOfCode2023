import sys
from functools import reduce
from operator import mul


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print (f'Usage: {sys.argv[0]} input_file')
        sys.exit(-1)
    
    # parse each line from input file
    file_name = sys.argv[1]
    lines = []
    with open(file_name, 'r') as file:
        lines = file.readlines()

    res = 0
    for i, game in enumerate(lines):
        items = game.split(':')[1].strip('\n').split(';')
        
        # compute max value of items from current game
        # that would be the minimum value required to play the game
        max_cubes = {}
        for item in items:
            for c_b_pair in item.split(','):
                count, ball = c_b_pair.strip(' ').split(' ')
                max_cubes[ball] = int(count) if max_cubes.get(ball) is None else max(max_cubes[ball], int(count))
                
        res += reduce(mul, max_cubes.values())
            
    print (res)


        