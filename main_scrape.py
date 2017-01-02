""" Scrape website for fantasy football stats """
from bs4 import BeautifulSoup
import urllib.request
from lxml import html

class RBWR:
    def __init__(self, name, team, attempts, rushyd, rushtd, targets,
                receptions, recyd, recTD, games_played, fpoints, fppg):
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

#    def print_stats(self):


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

#    def print_stats(self):


team = []
url = 'http://www.fftoday.com/stats/playerstats.php?Season=2016&GameWeek=&PosID='

pos = 'RB'

if pos == 'QB':
    url += '10'
elif pos == 'RB':
    url += '20&LeagueID=1'
elif pos == 'WR':
    url += '30&LeagueID=1'

# gets webpage with stats
page = urllib.request.urlopen(url).read()

soup = BeautifulSoup(page, "lxml")
col_count =0
player_array = []
for row in soup.find_all('td', class_='sort1'):
#    print(row.text)
    player_array.append(row.text)
