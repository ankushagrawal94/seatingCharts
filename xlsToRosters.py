def findnth(fullStr, shortStr, n):
    parts= fullStr.split(shortStr, n+1)
    if len(parts)<=n+1:
        return -1
    return len(fullStr)-len(parts[-1])-len(shortStr)

def getStudents():
  numSections = html_str.count("Section Name:")
  for i in xrange(0, numSections):
    sectionIdx = findnth(html_str, "Section Name:", i)
    numStudents = html_str.count("MAILTO:", sectionIdx, findnth(html_str, "Section Name:", i+1))
    nextStudent = sectionIdx
    section = []
    for j in xrange(0, numStudents):
      nextSign = '</td><td>'
      home = html_str.find(nextSign, nextStudent)
      nextSign = '<td>'
      idxOfName = html_str.rfind(nextSign, 0, home)
      stuName = html_str[idxOfName+4: home]

      nextSign = '</td><td>'
      endOfPID = html_str.find(nextSign, home+1)
      pid = html_str[home+9: endOfPID]

      newStart = html_str.find('>', endOfPID)
      for i in range(0,2):
        newStart = html_str.find('>', newStart+1)
      idxOfEmailEnd = html_str.find('<', newStart)
      email = html_str[newStart+1: idxOfEmailEnd]
      #print stuName + '\t' + pid + '\t' + email
      section.append([stuName, pid, email])

      nextStudent = idxOfEmailEnd + 100

    sections.append(section)

def randomizeSeating():
  for j in range(0,11):
    random.shuffle(sections[j], random.seed(datetime.datetime.now().isocalendar()[1]))
    i = 1
    for student in sections[j]:
      if i > 42:
        if i%2==0:
            student.append((i-44)*2+2)
        else:
            student.append((i-43)*2+2)
      else:
        if i%2 == 0:
            student.append(i-1)
        else:
            student.append(i)
      i+=1

def outputFiles():
  for idx, val in enumerate(sections):
    g = open ('rosters/'+ 'roster.' + sectionNames[idx], 'w')
    e = open ('rosters/'+ 'roster.'+ sectionNames[idx] +'.txt', 'w')
    h = open ('rosters/'+ sectionNames[idx] + '.txt', 'w')
    for student in sections[idx]:
      g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
      e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
      h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
    g.close()
    h.close()
    e.close()

import random
import datetime

f = open('sections.xls', 'r')
html_str = ""
sectionNames = ["W4", "W6", "W8", "Th9", "Th11", "Th1", "Th3", "Th5", "Th7", "F10", "F12"]
sections = []

for line in f:
  if line.count("<td>Student Name") != 0:
    continue
  if line.count("Students not in a section") != 0:
    break
  html_str += line

getStudents()
randomizeSeating()
outputFiles()

#print sections
