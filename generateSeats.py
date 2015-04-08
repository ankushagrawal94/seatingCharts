import csv, random

W4 = []
W6 = []
W8 = []
Th9 = []
Th11 = []
Th1 = []
Th3 = []
Th5 = []
Th7 = []
F10 = []
F12 = []

section = [W4, W6, W8, Th9, Th11, Th1, Th3, Th5, Th7, F10, F12]
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
         print student

#print "Generating Text Files" '\n'
for j in range(0,10):
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

g = open ('roster.W4', 'w')
e = open ('roster.W4.txt', 'w')
h = open ('W4.txt', 'w')
for student in section[0]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.W6', 'w')
e = open ('roster.W6.txt', 'w')
h = open ('W6.txt', 'w')
for student in section[1]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.W8', 'w')
e = open ('roster.W8.txt', 'w')
h = open ('W8.txt', 'w')
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

g = open ('roster.Th7', 'w')
e = open ('roster.Th7.txt', 'w')
h = open ('Th7.txt', 'w')
for student in section[6]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.F10', 'w')
e = open ('roster.F10.txt', 'w')
h = open ('F10.txt', 'w')
for student in section[6]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

g = open ('roster.F12', 'w')
e = open ('roster.F12.txt', 'w')
h = open ('F12.txt', 'w')
for student in section[6]:
    g.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    e.write (student[0] + '\t' + student[1] + '\t' + student[2] + '\t' +"%d" % (student[len(student) - 1]) + '\n')
    h.write (student[0] + '\t' + "%d" % (student[len(student) - 1]) + '\n')
g.close()
h.close()
e.close()

#print "Script Complete" '\n'