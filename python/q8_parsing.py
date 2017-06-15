# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
with open('football.csv') as csvfile:
    data = csv.reader(csvfile)
    scoreList = []
    for row in data:
        if len(row) != 0:
            scoreList = scoreList + [row]
csvfile.close()
index = 1
dif = abs(int(scoreList[1][6]) - int(scoreList[1][5]))
for i in range(2,len(scoreList)):
    if (abs(int(scoreList[i][6]) - int(scoreList[i][5]))) < dif:
        index = i
        dif = abs(int(scoreList[i][6]) - int(scoreList[i][5]))
print(scoreList[index][0])

