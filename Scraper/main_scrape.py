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

    pos = (input("Which position would you like to search: \n ---> ")).upper()
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
        print('  {})\t'.format(len(pobject_array)),player.get_name())
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
        if item.get_name() == pick_player:
            item.print_stats()
            player = item
            print()
        else:
            continue

    pos = player.get_pos()
    see_more = input('Would you like to view more of {}\'s stats? (Y/N): '.format(player.get_name()))
    # give options for stats if yes
    if see_more.upper() == 'Y':
        while see_more.upper() == 'Y':
            if pos == 'QB':
                print("-------------------------\n 1) Games Played \t|\n 2) Attempts \t\t|\n 3) Completions \t|\n 4) Rush Yds \t\t|")
                print(" 5) Rush TDs \t\t|\n 6) Rush Attempts \t|\n 0) Exit \t\t|\n-------------------------")
                stat_num = (input('Enter Number -> '))
                if stat_num == '0':
                    break
                print('>> ', player.print_more(stat_num))

            elif pos == 'RB':
                print("-------------------------\n 1) Games Played \t|\n 2) Attempts \t\t|\n 3) Rush TDs \t\t|\n 4) Targets \t\t|")
                print(" 5) Receptions \t\t|\n 6) Rec TDs \t\t|\n 0) Exit \t\t|\n-------------------------")
                stat_num = (input('Enter Number -> '))
                if stat_num == '0':
                    break
                print('>> ', player.print_more(stat_num))

            else:
                print("-------------------------\n 1) Games Played \t|\n 2) Targets \t\t|\n 3) Rec TD \t\t|\n 4) Rush Attempts \t|")
                print(" 5) Rush YDs \t\t|\n 6) Rush TDs \t\t|\n 0) Exit \t\t|\n-------------------------")
                stat_num = (input('Enter Number -> '))
                if stat_num == '0':
                    break
                print('>> ', player.print_more(stat_num))

    # check if another search is necessary
    new_search = input('Would you like to search another players stats? (Y/N): ')
    if new_search.upper() == 'Y':
        continue
    # end if done
    else:
        print('Goodbye!')
        break
