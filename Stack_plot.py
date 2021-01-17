import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# element input to plt is in list or array-like
# mintues in games
minutes = [1,2,3,4,5,6,7,8,9]

# play a videos game and have team keep track total points for whole team, and how many points each player contributed
# how many points 1 player contributed in each elem mintues
# at minutes[0] = 1 total points = player1[0]+..+player3[0]
player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['player1','player2','player3']
colors = ['#6d904f','#fc4f30','#008fd5']

# pie_chart hard code in [1,1,1] is the point of 2 player in 1st mintues
# plt.pie([1,1,1], labels=['player1','player2','player3'])

# stack plot is really good for data where you wanna track total and see a breakdown of total by a specific catefories
plt.stackplot(minutes,player1,player2,player3, labels=labels,colors=colors)

# call legend to show legend
plt.legend(loc='upper left')

plt.title('My Awesome Stack Plot')
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
