import csv
import itertools
from itertools import islice
import pprint
from pprint import pprint

lastnamedic = {}
fullnamedic = {}
with open ('faculty.csv') as csvfile:
    data = csv.reader(csvfile)
    next(data, None)
    for row in data:
        ln = row[0].split()[-1]
        firstn = row[0].split()[0]
        fn = (firstn,ln)
        if ln in lastnamedic:
            lastnamedic[ln].extend([row[1:]])
        else:
            lastnamedic[ln] = [row[1:]]
        if fn in fullnamedic:
            fullnamedic[fn].extend([row[1:]])
        else:
            fullnamedic[fn] = [row[1:]]
csvfile.close()

x = sorted(lastnamedic.items())
pprint(x[:3])

y = sorted(fullnamedic.items(), key = lambda p:p[0][0])
pprint(y[:3])

z = sorted(fullnamedic.items(), key = lambda p: p[0][1])
pprint(z[:3])
