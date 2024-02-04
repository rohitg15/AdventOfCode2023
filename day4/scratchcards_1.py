import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print (f'Usage: {sys.argv[0]} input_file')
        sys.exit(-1)
    
    # parse each line from input file
    file_name = sys.argv[1]
    with open(file_name, "r") as file:
        lines = file.readlines()
    

    total = 0
    for line in lines:
        # parse wins, current values for current card
        _, vals = line.split(':')
        winstr, curstr = vals.strip(' ').split('|')

        # remove empty strings from split
        wins, curs = list( filter(None, winstr.strip(' ').split(' ') ) ), list( filter( None, curstr.strip(' ').strip('\n').split(' ') ) )
        
        num_matches = sum((1 if cur in wins else 0 for cur in curs))
        total = total + (1 << (num_matches - 1) ) if num_matches > 0  else total
    
    print (total)
