"""
    run.py takes paramters at the command line and returns all stats
    for the given player

    ex: python3 run.py [position] [player name]

    """

import sys
from scraper import *

try:
    p_list = create_list(sys.argv[1])
    player = find_player(p_list, ''.join(sys.argv[2]))
    player.print_stats()
except AttributeError:
    print("That isn't a valid player! Try again.")
