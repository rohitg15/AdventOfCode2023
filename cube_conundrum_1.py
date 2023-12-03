import sys


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

    # elf's bag contains the following
    bag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    res = 0
    for i, game in enumerate(lines):
        items = game.split(':')[1].strip('\n').split(';')
        is_game_possible = True
        for item in items:
            cubes = {}
            # accumulate each color cube's respective count for this game
            for c_b_pair in item.split(','):
                count, color_cube = c_b_pair.strip(' ').split(' ')
                cubes[color_cube] = int(count) if cubes.get(color_cube) is None else cubes[color_cube] + int(count)
                
            # check if elf's bag has enough color cubes to play this game
            if any(bag.get(cube) is not None and bag[cube] < count for cube, count in cubes.items()):
                is_game_possible = False
        
        if is_game_possible:
            res += (i + 1)
            
    print (res)


        