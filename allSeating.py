import sys, time, fileinput

labNumber = raw_input("What is the lab number? \n")
weekNumber = raw_input("What is the week number? \n")
date = raw_input("What is the date? Ex April 8, 2014 \n")

x = fileinput.FileInput("seatme",inplace=1)
for line in x:
    if 'TEST=' in line:
        ogLine = line
        newLine = 'TEST=\"Lab ' + labNumber + '\"'
        line = line.replace(ogLine, newLine)

x.close()
