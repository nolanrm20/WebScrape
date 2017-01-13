"""
    run.py takes paramters at the command line and returns all stats
    for the given player

    ex: python3 run.py qb 'aaron rodgers'

    this would return the stats for aaron rodgers

    """

import sys
from main_scrape import *

try:
    p_list = create_list(sys.argv[1])
    player = find_player(p_list, ''.join(sys.argv[2]))
    player.print_stats()
except AttributeError:
    print("That isn't a valid player! Try again.")
