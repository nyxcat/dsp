import csv

degree = {}
title = {}
emaildomain = {}
degreedata = []
titledata = []
emaildata = []

with open('faculty.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ',')
    for row in data:
        degreedata.append(row[1].split())
        titledata.append(row[2])
        emaildata.append(row[3])
csvfile.close()

#the frequencies of degrees
for i, p in enumerate(degreedata):
    for j, d in enumerate(p):
        degreedata[i][j] = d.replace('.','')
        if degreedata[i][j] in degree:
            degree[degreedata[i][j]] += 1
        else:
            degree[degreedata[i][j]] = 1
del degree['degree']
del degree['0']
print('There are %i degrees.' %len(degree))
print(degree)

#the frequencies of title
for i, p in enumerate(titledata):
    if p[0] == 'P':
        titledata[i] = ' '.join(p.split()[:1])
    else:
        titledata[i] = ' '.join(p.split()[:2])
    if titledata[i] in title:
        title[titledata[i]] += 1
    else:
        title[titledata[i]] = 1
del title['title']
print('There are %i titles.' %len(title))
print(title)

#emaillist
emaildata.pop(0)
print('The email list is:')
print(emaildata)

#emaildomains
for i, p in enumerate(emaildata):
    emaildata[i] = p.split('@')
    if emaildata[i][1] in emaildomain:
        emaildomain[emaildata[i][1]] += 1
    else:
        emaildomain[emaildata[i][1]] = 1
print('There are %i emaildomains.' %len(emaildomain))
print(emaildomain)
