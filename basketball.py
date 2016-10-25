class Game(object):
    def __init__(self, home_name, away_name):
        self.home_name = home_name
        self.away_name = away_name

    def setResult(self, total, quarters):
        self.result = Result(total, quarters)

    def getResult(self):
        return self.result

    def setHomeStats(self, stat_row):
        self.home_stats = stat_row
    
    def getHomeStats(self):
        return self.home_stats

    def setAwayStats(self, stat_row):
        self.away_stats = stat_row
    
    def getAwayStats(self):
        return self.away_stats

    def setGameDate(self, date):
        self.date = date

    def setGameRefId(self, ref_id):
        self.ref_id = ref_id

    def setGameNr(self, game_nr):
        self.game_nr = game_nr

    

    def write(self):
        print(self.home_name + " vs " + self.away_name)
        print("game nr: " + self.game_nr)
        print("date: " + self.date)
        #print(str(self.homeResult.getScore()) + " " + str(self.awayResult.getScore()))
        print(self.result.getScore())
        print(self.result.getScoreQuarters())
        #self.homeStats.Write()
        #self.awayStats.Write()



class Result(object):
    def __init__(self, score, quarters):
        self.score = score
        self.quarters = quarters

    def getScore(self):
        return self.score

    def getScoreQuarters(self, q=0):
        if (q == 0):
            return self.quarters
        else:
            return [self.quarters[0][q-1], self.quarters[1][q-1]] 

    def getHalftimeScore(self):
        return [self.quarters[0][0]+self.quarters[0][1], self.quarters[1][0] + self.quarters[1][1]]

class TeamStatRow(object):    
    
    def __init__(self, statrow):
        self.names = ['min','two_s','two_t','two_pct','three_s','three_t','three_pct','one_s','one_t','one_pct','reb_o','reb_d','reb_tot','ass','foul','to','stl','blk','eff','points']
        self.min = statrow[0]
        self.two_s = statrow[1]
        self.two_t = statrow[2]
        self.two_pct = statrow[3]
        self.three_s = statrow[4]
        self.three_t = statrow[5]
        self.three_pct = statrow[6]
        self.one_s = statrow[7]
        self.one_t = statrow[8]
        self.one_pct = statrow[9]
        self.reb_o = statrow[10]
        self.reb_d = statrow[11]
        self.reb_tot = statrow[12]
        self.ass = statrow[13]
        self.foul = statrow[14]
        self.to = statrow[15]
        self.stl = statrow[16]
        self.blk = statrow[17]
        self.eff = statrow[18]
        self.points = statrow[19]
        self.row = statrow
        self.team_name = ""

    def setTeamName(self, name):
        self.team_name = name
    
    def write(self):
        
        for i in range(len(self.names)):
            print(self.names[i] + ": " + str(self.row[i]))
# class Stats(object):
#     def __init__(self):
#         self.val = ""

# class BoxScore(object):


#     def write(self):
#         for i in self.all:
#             print(value)

    # def setAll(self, boxscore):
    #     self.one_s = boxscore[0]
    #     self.one_t = boxscore[1]
    #     self.one_pct = boxscore[2]
    #     self.two_s = boxscore[3]
    #     self.two_t = boxscore[4]
    #     self.two_pct = boxscore[5]
    #     self.three_s = boxscore[6]
    #     self.three_t = boxscore[7]
    #     self.three_pct = boxscore[8]
    #     self.reb_o = boxscore[9]
    #     self.reb_d = boxscore[10]
    #     self.reb_tot = boxscore[11]
    #     self.ass = boxscore[12]
    #     self.foul = boxscore[13]
    #     self.to = boxscore[14]
    #     self.stl = boxscore[15]
    #     self.eff = boxscore[16]
    #     self.plus_minus = boxscore[17]
    #     self.points = boxscore[18]


class PlayerBoxScore(object):
    def __init__(self):
        self.val = ""



class Odds(object):
    def __init__(self, time, home_name, away_name, home_odds, away_odds, game_id):
        self.time = time

def getGameName(nameish):

    gamelist = [
    ["BC Luleå", "BC Lulea"],
    ["Borås Basket", "Boras"],
    ["Jämtland Basket", "Jamtland"],
    ["KFUM Nässjö", "Nassjo"],
    ["LF Basket", "LF Basket"],
    ["Malbas", "Malbas"],
    ["Norrköping Dolphins", "Norrkoping"],
    ["Solna Vikings", "Solna"],
    ["Sundsvall Dragons", "Sundsvall"],
    ["Södertälje Kings", "Sodertalje"],
    ["Umeå BSKT", "Umea"],
    ["Uppsala Basket", "Uppsala"],
    ["ecoÖrebro", "Orebro"]
    ]

    for i in gamelist:
        if (i[1] == nameish):
            return i[0]








