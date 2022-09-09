from mplsoccer import Sbopen
import math
from statistics import mean


##### LINKS TO SOURCES #####
# https://www.mondefootball.fr/buteurs/em-2020/
# https://www.youtube.com/watch?v=-uQV-jGeRXQ


##### OPENING COMPETITION DATA SET #####

parser = Sbopen()
dataFrameCompetition = parser.competition()


##### SETTING VARIABLE OF INTEREST #####

# ID of Euro 2020
competitionId = 55
seasonID = 43


##### OPENING EURO2020 MATCH DATA SET #####

dataFrameMatch = parser.match(competitionId, seasonID)


##### GET xgAverage AND nShot VARIABLES FOR EACH PLAYER #####

xgListAll = []

xgListRonaldo = []
xgListSchick = []
xgListBenzema = []
xgListForsberg = []
xgListKane = []
xgListLukaku = []

for matchId in dataFrameMatch["match_id"]:
    dataFrameEvent = parser.event(matchId)[0]
    for  playerName, xgValue in dataFrameEvent[['player_name','shot_statsbomb_xg']].itertuples(index=False):
        if math.isnan(xgValue) is False :
            xgListAll.append(xgValue)
            if playerName == "Cristiano Ronaldo dos Santos Aveiro":
                xgListRonaldo.append(xgValue)
            elif playerName == "Patrik Schick":
                xgListSchick.append(xgValue)
            elif playerName == "Karim Benzema":
                xgListBenzema.append(xgValue)
            elif playerName == "Emil Peter Forsberg":
                xgListForsberg.append(xgValue)
            elif playerName == "Harry Kane":
                xgListKane.append(xgValue)
            elif playerName == "Romelu Lukaku Menama":
                xgListLukaku.append(xgValue)        
        
xgAverageAll = mean(xgListAll)

xgAverageRonaldo = mean(xgListRonaldo)
nShotRonaldo = len(xgListRonaldo)

xgAverageBenzema = mean(xgListBenzema)
nShotBenzema = len(xgListBenzema)

xgAverageKane = mean(xgListKane)
nShotKane = len(xgListKane)

xgAverageLukaku = mean(xgListLukaku)
nShotLukaku = len(xgListLukaku)

xgAverageSchick = mean(xgListSchick)
nShotSchick = len(xgListSchick)

xgAverageForsberg = mean(xgListForsberg)
nShotForsberg = len(xgListForsberg)