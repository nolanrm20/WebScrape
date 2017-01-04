""" Scrape website for fantasy football stats

    Will have you input a position and player and
    will give you their stats from 2016 season
"""
from bs4 import BeautifulSoup
import urllib.request
from lxml import html
from player import *

# site to be scraped
url = 'http://www.fftoday.com/stats/playerstats.php?Season=2016&GameWeek=&PosID='

pos = (input("What position is the player: \n ---> "))
player_name = (input("Players name: \n ---> "))
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
for item in player_array:
    if item == player_name:
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
        break
    else:
        count += 1

# print player when found
player.print_stats()
while(True):
    see_more = input('Would you like to view another stat? (Y/N): ')

    if see_more.upper() == 'Y':
        if pos == 'QB':
            print("-------------------\n 1) Games Played \n 2) Attempts \n 3) Completions \n 4) Rush Yds ")
            print(" 5) Rush TDs \n 6) Rush Attempts \n -------------------")
            stat_num = (input('>> '))
            print('>> ', player.print_more(stat_num))

        elif pos == 'RB':
            print("-------------------\n 1) Games Played \n 2) Attempts \n 3) Rush TDs \n 4) Targets ")
            print(" 5) Receptions \n 6) Rec TDs \n -------------------")
            stat_num = (input('>> '))
            print('>> ', player.print_more(stat_num))

        else:
            print("-------------------\n 1) Games Played \n 2) Targets \n 3) Rec TD \n 4) Rush Attempts")
            print(" 5) Rush YDs \n 6) Rush TDs \n -------------------")
            stat_num = (input('---> '))
            print('>> ', player.print_more(stat_num))
    else:
        break
