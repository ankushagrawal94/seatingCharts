import datetime
import time

week0 = 12 #change this for new quarter


def next_weekday(d, weekday): # Weekday represents day of week 0 = Monday, 1=Tuesday, 2=Wednesday...
    days_ahead = weekday - d.weekday()
    if days_ahead < 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def findNextDay(sectionName):
  if sectionName.count('W') != 0:
    return 2
  elif sectionName.count('Th') != 0:
    return 3
  elif sectionName.count('T') != 0:
    return 1
  elif sectionName.count('F') != 0:
    return 4

sectionNames = ["W4", "W6", "W8", "Th9", "Th11", "Th1", "Th3", "Th5", "Th7", "F10", "F12"]

for section in sectionNames:
  d = datetime.datetime.now()
  nextWeek = next_weekday(d, findNextDay(section))
  newDate = ("%s %s, %s" % ((time.strftime("%b", nextWeek.timetuple()), nextWeek.day, nextWeek.year)))
  weekNum = nextWeek.date().isocalendar()[1] - week0
  labNum = str(weekNum - 1)
  f = open('rosters/'+'seatme'+  section, 'r')
  fullTxt = ""
  for line in f:
    if line.count("TEST=") != 0:
      line = "TEST=" + "\"" + "Lab " + labNum + "\"" + '\n'
    if line.count("WEEK=") != 0:
      line = "WEEK=" + str(weekNum) + '\n'
    if line.count("DATE=") != 0:
      line = "DATE=\"" + newDate + '\"\n'
    fullTxt += str(line)

  g = open('rosters/'+'seatme'+ section, 'wb')
  g.write(fullTxt)
