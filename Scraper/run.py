"""
    run.py takes paramters at the command line and returns all stats
    for the given player

    ex: python3 run.py [position] [player name]
     OR python3 run.py [position] [player 1] [player 2]

    """

import sys
from scraper import *

if len(sys.argv) == 4:
    p_list = create_list(sys.argv[1])
    p1 = ''.join(sys.argv[2])
    p2 = ''.join(sys.argv[3])
    compare_players(p_list, p1, p2)

else:
    try:
        p_list = create_list(sys.argv[1])
        player = find_player(p_list, ''.join(sys.argv[2]))
        player.print_stats()
    except AttributeError:
        print("That isn't a valid player! Try again.")
