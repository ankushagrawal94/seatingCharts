import csv, sys

g = open('roster.' + sys.argv[1] + 'short.txt', 'w')
#g = open ('roster.Tu9short.txt', 'w')
with open('/Development/15lseating.bak/roster.' + sys.argv[1] + '.txt','rU') as f:
    reader=csv.reader(f,delimiter='\t')
    for student in reader:
        g.write(student[0] + '\t' + student[3] + '\n')
g.close()
