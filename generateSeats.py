import csv, random

W3 = []
W7 = []
Th9 = []
Th11 = []
Th1 = []
Th3 = []
Th5 = []

section = [W3, W7, Th9, Th11, Th1, Th3, Th5]
temp = []

with open('/Development/seatingCharts/sections.txt','rU') as f:
    reader=csv.reader(f,delimiter='\t')
    next(f)
    next(f)
    i = 0;
    x = 1;
    temp = section[i]
    for student in reader:
        if student[0][:12] == "Section Name":
            i = i+1
            temp = section[i]
            next(f)
            continue
        if student[0] == "Students not in a section":
            break
        if len(student[0])!=0:
         temp.append(student)

#print "Generating Text Files" '\n'
for j in range(0,7):
    random.shuffle(section[j])
    i = 1
    for student in section[j]:
        if i > 42:
            if i%2==0:
                student.append(i-42)
            else:
                 student.append(i-41)
        else:
            if i%2 == 0:
                student.append(i-1)
            else:
                student.append(i)
        i+=1

g = open ('roster.W3', 'w')
e = open ('roster.W3.txt', 'w')
h = open ('W3.txt', 'w')
for student in section[0]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.W7', 'w')
e = open ('roster.W7.txt', 'w')
h = open ('W7.txt', 'w')
for student in section[1]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.Th9', 'w')
e = open ('roster.Th9.txt', 'w')
h = open ('Th9.txt', 'w')
for student in section[2]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.Th11', 'w')
e = open ('roster.Th11.txt', 'w')
h = open ('Th11.txt', 'w')
for student in section[3]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.Th1', 'w')
e = open ('roster.Th1.txt', 'w')
h = open ('Th1.txt', 'w')
for student in section[4]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.Th3', 'w')
e = open ('roster.Th3.txt', 'w')
h = open ('Th3.txt', 'w')
for student in section[5]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.Th5', 'w')
e = open ('roster.Th5.txt', 'w')
h = open ('Th5.txt', 'w')
for student in section[6]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

#print "Script Complete" '\n'