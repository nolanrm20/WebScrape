"""
    main_scrape.py contains the create_list function

    this takes in a position, scrapes a site for stats,
    and creates a list of player objects (RB, WR, QB) of
    the top 50 players at that position
"""
from bs4 import BeautifulSoup
import urllib.request
from lxml import html
from player import *

def create_list(pos):
    """ Gets input from user of position to search

        returns a list of top 50 players at that position
     """

    # site to be scraped
    url = 'http://www.fftoday.com/stats/playerstats.php?Season=2016&GameWeek=&PosID='

    pos = ''.join(pos).upper()
    col_max = 0
    # get correct web url
    if pos == 'QB':
        url += '10'
        col_max = 12
    elif pos == 'RB':
        url += '20&LeagueID=1'
        col_max = 11
    elif pos == 'WR':
        url += '30&LeagueID=1'
        col_max = 11

    # gets webpage with stats
    page = urllib.request.urlopen(url).read()

    # create beautiful soup object from page
    soup = BeautifulSoup(page, "lxml")
    col_count =0
    player_array = []

    for row in soup.find_all('td', class_='sort1'):
        # name is a hyperlink so find and get text
        if col_count == 0:
            player_array.append(row.find('a').text)
            col_count += 1
        elif col_count == col_max:
            player_array.append(row.text)
            col_count = 0
        else:
            player_array.append(row.text)
            col_count += 1

    # search for and find player in list
    # create player item
    count = 0
    players = []

    while(count < len(player_array)):
        if pos == 'QB':
            player = QB(*player_array[count:count+13])

        elif pos == 'RB':
            player = RB(*player_array[count:count+12])

        else:
            player = WR(*player_array[count:count+12])

        # add player to list
        players.append(player)
        count += col_max + 1

    return players

def find_player(player_list, player):
    """
        param player_list: list of player objects
              player: name of player you are searching for

        returns player object of specified player if found
        return 0 if not found

    """
    for item in player_list:
        if item.name.upper() == player.upper():
            return item

    return 0

def compare_players(player_list, player1, player2):
    """
        param player_list: list of player objects
              player1: name of first player
              player2: name of second player

        prints stats of two players being compared or throws exception
        if invalid names are entered
    """
    try:
        p1 = find_player(player_list, player1)
        p2 = find_player(player_list, player2)
        p1.print_stats()
        p2.print_stats()
    except AttributeError:
        print('At least one of those players was invalid. Try again.')
