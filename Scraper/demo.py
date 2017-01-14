"""
    demo.py will take input from user for position and player
    it will also allow you to view multiple players stats, and
    decide if you want to see more stats for them

    """

from scraper import *

while(True):
    
    pos = (input("Which position would you like to search: (QB, RB, WR)\n ---> ")).upper()
    # get list of players
    list_of_players = create_list(pos)

    print('-----------------------------')
    print('|           Name            |')
    print('-----------------------------')
    for index, item in enumerate(list_of_players):
        print('  {})\t'.format(index + 1),item.name)


    # get input for player to search
    while(True):
        try:
            pick_player = input('Which players stats would you like to find? : ')
            print()
            player = find_player(list_of_players, pick_player)
            player.print_stats()
            break
        except AttributeError:
            print("That isn't a valid player! Try again.")


    # check if another search is necessary
    new_search = input('Would you like to search another players stats? (Y/N): ')
    if new_search.upper() == 'N':
        print('Goodbye!')
        break
