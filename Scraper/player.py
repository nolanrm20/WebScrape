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
        print("*----------------------------------------*")
        print("Name: \t\t", self.name, "\nTeam: \t\t", self.team, "\nTDs: \t\t", int(self.rushTD) + int(self.recTD),
            "\nRush Yd: \t", self.rushyd, "\nRec Yd: \t", self.recyd, "\n", self.name, " scored ", self.fppg, " points per game played")
        print("* Fantasy Points {} *".format(self.fpoints))
        print("*----------------------------------------*")

    def print_more(self):
        print("-----------------------------")
        print(" Games Played \t\t{}\n Attempts \t\t{}\n Rush TDs \t\t{}".format(self.games_played, self.attempts, self.rushTD))
        print(" Targets \t\t{}\n Receptions \t\t{}\n Rec TDs \t\t{}".format(self.targets, self.receptions, self.recTD))
        print("-----------------------------")

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
        print("*----------------------------------------*")
        print("Name: \t\t", self.name, "\nTeam: \t\t", self.team, "\nTDs: \t\t", int(self.rushTD) + int(self.recTD),
            "\nRec Yd: \t", self.recyd, "\nReceptions: \t", self.receptions, "\nTargets: \t", self.targets,
            "\n", self.name, " scored ", self.fppg, " points per game played")
        print("* Fantasy Points {} *".format(self.fpoints))
        print("*----------------------------------------*")

    def print_more(self):
        print("-----------------------------")
        print(" Games Played \t\t{}\n Targets \t\t{}\n Rec TD \t\t{}".format(self.games_played, self.targets, self.recTD))
        print(" Rush Attempts \t\t{}\n Rush YDs \t\t{}\n Rush TDs \t\t{}".format(self.attempts, self.rushyd, self.rushTD))
        print("-----------------------------")

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
        print("*----------------------------------------*")
        print("Name: \t\t", self.name, "\nTeam: \t\t", self.team, "\nPass TDs: \t", self.TD,
            "\nPass Yd: \t", self.yards, "\nInts: \t\t", self.ints, "\n", self.name, " scored ", self.fppg, " points per game played")
        print("* Fantasy Points {} *".format(self.fpoints))
        print("*----------------------------------------*")

    def print_more(self):
        print("------------------------------")
        print(" Games Played \t\t{}\n Attempts \t\t{}\n Completions \t\t{}".format(self.games, self.attempts, self.completions))
        print(" Rush Yds \t\t{}\n Rush TDs \t\t{}\n Rush Attempts \t\t{}".format(self.rushyd, self.rushTD, self.rushes))
        print("------------------------------")
