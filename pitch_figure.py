from   mplsoccer import Sbopen 
import matplotlib.pyplot as plt
from mplsoccer import Pitch


##### OPENING COMPETITION DATA SET #####

parser = Sbopen()
dataFrameCompetition = parser.competition()


##### SETTING VARIABLE OF INTEREST #####

# ID of Euro 2020
competitionId = 55
seasonID = 43
matchId = 3788748


##### GET SHOT AND PLAYER POSITIONS FROM SCOTLAND VS CZECH REPUBLIC EVENT DATA SET #####

dataFrameEvent = parser.event(matchId)


for  i, xgValue, x, y, end_x, end_y in dataFrameEvent[0][['index','shot_statsbomb_xg','x','y','end_x','end_y']].itertuples(index=False):
    if i == 1987:
        xg = xgValue
        xShot = x
        yShot = y
        xEnd = end_x
        yEnd= end_y
    elif i == 1988:
        xGoalkeeper = x
        yGoalkeeper = y

             

##### DRAW THE PITCH #####

# Generate the figure 
fig = plt.figure(figsize = (4,4), dpi = 600)
ax = plt.subplot(111)
ax2 = plt.subplot(111)


# Draw the actual pitch on the figure
pitch = Pitch(
                  pitch_type = "statsbomb",
                  half = True,
                  label = False,
                  tick = False,
                  goal_type='box',
                  linewidth = 3,
                  line_color = 'grey'
              )
pitch.draw(ax = ax)


##### DRAW THE SHOT #####

# Draw the player as a hashed circle
schickCircle = pitch.scatter(
                        xShot,
                        yShot,
                        s=100,
                        edgecolors='lightcoral',
                        c='None',
                        hatch='//////',
                        marker='o',
                        ax=ax
                    )

goalkeeperCircle = pitch.scatter(
                        120 - xGoalkeeper,
                        80 - yGoalkeeper,
                        s=100,
                        edgecolors='cornflowerblue',
                        c='None',
                        hatch='//////',
                        marker='o',
                        ax=ax2
                    )

# Draw the shot as a dotted line
ax.plot([xShot, xEnd], [yShot, yEnd], color = "peru", ls = ":")


##### SAVE THE FIGURE #####

fig.set_size_inches(5, 5)
fig.savefig('output/pitch_figure.png', dpi = 800, transparent=True)