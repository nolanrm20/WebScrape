""" Classes for creating player objects

    print_stats is run in main_scrape when a user inputs a player

    print_more is essentially a switch statement that returns a stat
    using the number input in main_scrape if user wants to view more
"""

class RB:
    def __init__(self, name, team, games_played, attempts, rushyd, rushtd, targets,
                receptions, recyd, recTD, fpoints, fppg):
        self.pos = 'RB'
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
        print("*------------|", self.name, "|---------------*")
        print("\nTeam \t\t\t", self.team, "\nGames Played \t\t", self.games_played, "\nTDs \t\t\t", int(self.rushTD) + int(self.recTD),
            "\nRush Yd \t\t", self.rushyd, "\nRec Yd \t\t\t", self.recyd)
        print("Attempts \t\t", self.attempts, "\nRush TDs \t\t", self.rushTD)
        print("Targets \t\t", self.targets, "\nReceptions \t\t",self.receptions,"\nRec TDs \t\t", self.recTD)
        print("FANTASY POINTS \t\t", self.fpoints, '\n')
        print(self.name, " scored ", self.fppg, " points per game played")
        print("*---------------------------------------------*")

class WR:
    def __init__(self, name, team, games_played, targets, receptions, recyd, recTD,
                attempts, rushyd, rushTD, fpoints, fppg):
        self.pos = 'WR'
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
        print("*------------|", self.name, "|---------------*")
        print("\nTeam \t\t\t", self.team, "\nGames Played \t\t", self.games_played, "\nTDs \t\t\t", int(self.rushTD) + int(self.recTD),
            "\nRec Yd \t\t\t", self.recyd, "\nReceptions \t\t", self.receptions)
        print("Targets \t\t", self.targets, "\nRec TD \t\t\t", self.recTD)
        print("Rush Attempts \t\t", self. attempts, "\nRush YDs \t\t", self.rushyd, "\nRush TDs \t\t", self.rushTD)
        print("FANTASY POINTS \t\t", self.fpoints, '\n')
        print(self.name, " scored ", self.fppg, " points per game played")
        print("*---------------------------------------------*")

class QB:
    def __init__(self, name, team, games, completions, attempts, yards,
                TD, ints, rushes, rushyd, rushTD, fpoints, fppg):
        self.pos = 'QB'
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
        print("*------------|", self.name, "|---------------*")
        print("\nTeam \t\t\t", self.team, "\nGames Played \t\t", self.games, "\nPass TDs \t\t", self.TD,
            "\nPass Yd \t\t", self.yards, "\nInts \t\t\t", self.ints)
        print("Attempts \t\t", self.attempts, "\nCompletions \t\t", self.completions)
        print("Rush Yds \t\t", self.rushyd, "\nRush TDs \t\t", self.rushTD, "\nRush Attempts \t\t",self.rushes)
        print("FANTASY POINTS \t\t", self.fpoints, "\n")
        print(self.name, " scored ", self.fppg, " points per game played")
        print("*---------------------------------------------*")
