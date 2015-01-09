def findnth(fullStr, shortStr, n):
    parts= fullStr.split(shortStr, n+1)
    if len(parts)<=n+1:
        return -1
    return len(fullStr)-len(parts[-1])-len(shortStr)

def getDetails(startPhrase):
  numAdded = html_str.count(startPhrase)
  for i in range(0, numAdded):
    addedByStartIdx = findnth(html_str, startPhrase, i)
    tmp = html_str[addedByStartIdx: addedByStartIdx + html_str[addedByStartIdx:].find('<')]
    addedBy = tmp[8:]

    newEnd = html_str[:addedByStartIdx].rfind('>')
    for i in range(0,5):
      newEnd = html_str[:newEnd-1].rfind('>')
    name = html_str[newEnd+1: newEnd + html_str[newEnd:].find('<')]

    tmp = html_str[addedByStartIdx + html_str[addedByStartIdx:].find("data-utime=") : addedByStartIdx + html_str[addedByStartIdx:].find("class=")]
    utime = tmp[12:len(tmp) - 2]
    
    if name not in name_dict:
      name_dict[name] = (name, addedBy, utime, startPhrase)
    print name + '\t' + addedBy + '\t' + utime

def getStudents():
  numSections = html_str.count("Section Name:")
  for i in xrange(0, numSections):
    sectionIdx = findnth(html_str, "Section Name:", i)
    numStudents = html_str.count("MAILTO:", sectionIdx, findnth(html_str, "Section Name:", i+1))
    nextStudent = sectionIdx
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

      print stuName + '\t' + pid + '\t' + email

      nextStudent = idxOfEmailEnd + 100



f = open('sections.xls', 'r')
html_str = ""
for line in f:
  if line.count("<td>Student Name") != 0:
    continue
  if line.count("Students not in a section") != 0:
    break
  html_str += line

getStudents()