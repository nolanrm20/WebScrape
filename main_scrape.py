""" Scrape website for fantasy football stats """
from bs4 import BeautifulSoup
import urllib.request
from lxml import html

class RB:
    def __init__(self, name, team, games_played, attempts, rushyd, rushtd, targets,
                receptions, recyd, recTD, fpoints, fppg):
        self.name = name
        self.team = team
        self.attempts = attempts
        self.rushyd = rushyd
        self.rushTD = rushtd
        self.targets = targets
        self.receptions = receptions
        self.recyd = recyd
        self.recTD = recTD
        self.games_played = games_played
        self.fpoints = fpoints
        self.fppg = fppg

    def print_stats(self):
        print("*------------------------------------*")
        print("Name: \t\t", self.name, "\nTeam: \t\t", self.team, "\nTDs: \t\t", int(self.rushTD) + int(self.recTD),
            "\nRush Yd: \t", self.rushyd, "\nRec Yd: \t", self.recyd, "\n", self.name, " scored ", self.fppg, " points per game")
        print("* Fantasy Points {} *".format(self.fpoints))
        print("*------------------------------------*")

class WR:
    def __init__(self, name, team, games_played, targets, receptions, recyd, recTD,
                attempts, rushyd, rushTD, fpoints, fppg):
        self.name = name
        self.team = team
        self.attempts = attempts
        self.rushyd = rushyd
        self.rushTD = rushTD
        self.targets = targets
        self.receptions = receptions
        self.recyd = recyd
        self.recTD = recTD
        self.games_played = games_played
        self.fpoints = fpoints
        self.fppg = fppg

    def print_stats(self):
        print("*------------------------------------*")
        print("Name: \t\t", self.name, "\nTeam: \t\t", self.team, "\nTDs: \t\t", int(self.rushTD) + int(self.recTD),
            "\nRec Yd: \t", self.recyd, "\nReceptions: \t", self.receptions, "\nTargets: \t", self.targets,
            "\n", self.name, " scored ", self.fppg, " points per game")
        print("* Fantasy Points {} *".format(self.fpoints))
        print("*------------------------------------*")

class QB:
    def __init__(self, name, team, games, completions, attempts, yards,
                TD, ints, rushes, rushyd, rushTD, fpoints, fppg):
        self.name = name
        self.team = team
        self.games = games
        self.completions = completions
        self.attempts = attempts
        self.yards = yards
        self.TD = TD
        self.ints = ints
        self.rushes = rushes
        self.rushyd = rushyd
        self.rushTD = rushTD
        self.fpoints = fpoints
        self.fppg = fppg

    def print_stats(self):
        print("*------------------------------------*")
        print("Name: \t\t", self.name, "\nTeam: \t\t", self.team, "\nPass TDs: \t", self.TD,
            "\nRush Yd: \t", self.rushyd, "\nInts: \t\t", self.ints, "\n", self.name, " scored ", self.fppg, " points per game")
        print("* Fantasy Points {} *".format(self.fpoints))
        print("*------------------------------------*")


team = []
url = 'http://www.fftoday.com/stats/playerstats.php?Season=2016&GameWeek=&PosID='

pos = (input("What position is the player: \n ---> "))
player_name = (input("Players name: \n ---> "))
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

soup = BeautifulSoup(page, "lxml")
col_count =0
player_array = []
for row in soup.find_all('td', class_='sort1'):
#    print(row.text)
    if col_count == 0:
        player_array.append(row.find('a').text)
        col_count += 1
    elif col_count == col_max:
        player_array.append(row.text)
        col_count = 0
    else:
        player_array.append(row.text)
        col_count += 1

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

player.print_stats()
