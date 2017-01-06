""" Scrape website for fantasy football stats

    Will have you input a position and player and
    will give you their stats from 2016 season
"""
from bs4 import BeautifulSoup
import urllib.request
from lxml import html
from player import *

def create_list():
    """ Gets input from user of position to search

        returns a list of top 50 players at that position
     """

    # site to be scraped
    url = 'http://www.fftoday.com/stats/playerstats.php?Season=2016&GameWeek=&PosID='

    pos = (input("Which position would you like to search: (QB, RB, WR)\n ---> ")).upper()

    col_max = 0
    # get correct web url
    if pos.upper() == 'QB':
        url += '10'
        col_max = 12
    elif pos.upper() == 'RB':
        url += '20&LeagueID=1'
        col_max = 11
    elif pos.upper() == 'WR':
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
    # create player item and print their name
    count = 0
    pobject_array = []
    print('-----------------------------')
    print('|Rank|        Name          |')
    print('-----------------------------')

    while(count < len(player_array)):
        if pos == 'QB':
            player = QB(player_array[count], player_array[count+1], player_array[count+2], player_array[count+3],
                        player_array[count+4], player_array[count+5], player_array[count+6], player_array[count+7],
                        player_array[count+8], player_array[count+9], player_array[count+10], player_array[count+11],
                        player_array[count+12])
        elif pos == 'RB':
            player = RB(player_array[count], player_array[count+1], player_array[count+2], player_array[count+3],
                        player_array[count+4], player_array[count+5], player_array[count+6], player_array[count+7],
                        player_array[count+8], player_array[count+9], player_array[count+10], player_array[count+11])
        else:
            player = WR(player_array[count], player_array[count+1], player_array[count+2], player_array[count+3],
                        player_array[count+4], player_array[count+5], player_array[count+6], player_array[count+7],
                        player_array[count+8], player_array[count+9], player_array[count+10], player_array[count+11])

        # add player to list
        pobject_array.append(player)
        print('  {})\t'.format(len(pobject_array)),player.name)
        count += col_max + 1

    return pobject_array

# main loop
while(True):

    # get list of players
    list_of_players = create_list()
    # get input for player to search
    pick_player = input('Which players stats would you like to find? : ')
    print()
    for item in list_of_players:
        if item.name == pick_player:
            item.print_stats()
            player = item
            print()

    pos = player.pos
    see_more = input('Would you like to view more of {}\'s stats? (Y/N): '.format(player.name))
    # give options for stats if yes
    if see_more.upper() == 'Y':

        if pos == 'QB':
            print("------------------------------")
            print(" Games Played \t\t{}\n Attempts \t\t{}\n Completions \t\t{}".format(player.games, player.attempts, player.completions))
            print(" Rush Yds \t\t{}\n Rush TDs \t\t{}\n Rush Attempts \t\t{}".format(player.rushyd, player.rushTD, player.rushes))
            print("------------------------------")

        elif pos == 'RB':
            print("-----------------------------")
            print(" Games Played \t\t{}\n Attempts \t\t{}\n Rush TDs \t\t{}".format(player.games_played, player.attempts, player.rushTD))
            print(" Targets \t\t{}\n Receptions \t\t{}\n Rec TDs \t\t{}".format(player.targets, player.receptions, player.recTD))
            print("-----------------------------")

        else:
            print("-----------------------------")
            print(" Games Played \t\t{}\n Targets \t\t{}\n Rec TD \t\t{}".format(player.games_played, player.targets, player.recTD))
            print(" Rush Attempts \t\t{}\n Rush YDs \t\t{}\n Rush TDs \t\t{}".format(player.attempts, player.rushyd, player.rushTD))
            print("-----------------------------")

    # check if another search is necessary
    new_search = input('Would you like to search another players stats? (Y/N): ')
    if new_search.upper() == 'Y':
        continue
    # end if done
    else:
        print('Goodbye!')
        break
