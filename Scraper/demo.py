"""
    demo.py will take input from user for position and player
    it will also allow you to view multiple players stats, and
    decide if you want to see more stats for them

    """

from main_scrape import create_list

while(True):

    pos = (input("Which position would you like to search: (QB, RB, WR)\n ---> ")).upper()
    # get list of players
    list_of_players = create_list(pos)

    print('-----------------------------')
    print('|           Name            |')
    print('-----------------------------')
    for index, item in enumerate(list_of_players):
        print('  {})\t'.format(index),item.name)


    # get input for player to search
    pick_player = input('Which players stats would you like to find? : ')
    print()
    for item in list_of_players:
        if item.name.upper() == pick_player.upper():
            item.print_stats()
            player = item
            print()

    pos = player.pos
    see_more = input('Would you like to view more of {}\'s stats? (Y/N): '.format(player.name))
    # show more stats if yes
    if see_more.upper() == 'Y':
        player.print_more()

    # check if another search is necessary
    new_search = input('Would you like to search another players stats? (Y/N): ')
    if new_search.upper() == 'N':
        print('Goodbye!')
        break
