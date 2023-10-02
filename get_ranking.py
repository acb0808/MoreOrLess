import csv
f = open('더많이더적게.csv', encoding='utf-16')
data = csv.reader(f)
next(data)

rankingMap = {}
origin = []
for i in data:
    origin.append((i[0],int(i[1])))

origin.sort(key=lambda x: x[1])

i = 1
for keyword in origin:
    rankingMap[keyword[0]] = i
    i += 1

import json
with open('ranking.json', 'w', encoding='utf-8')as f:
    f.write(json.dumps(rankingMap))