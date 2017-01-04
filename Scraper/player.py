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
