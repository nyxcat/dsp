#write to csv file

import csv

emaildata = []

with open ('faculty.csv') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        emaildata.append(row[3])
csvfile.close()

emaildata.pop(0)
with open ('emails.csv','w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    for item in emaildata:
        writer.writerow([item])
csvfile.close()
