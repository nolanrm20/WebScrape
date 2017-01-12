"""
    run.py takes paramters at the command line and returns all stats
    for the given player

    ex: python3 run.py qb 'aaron rodgers'

    this would return the stats for aaron rodgers

    """

import sys
from main_scrape import create_list

p_list = create_list(sys.argv[1])
for item in p_list:
    if item.name.upper() == ''.join(sys.argv[2]).upper():
        item.print_stats()
        item.print_more()
