import csv, sys, shlex

def alpha(day):
	g = open('roster.' + day + '.alpha.txt', 'w')
	with open('/Development/seatingCharts/roster.' + day + '.txt','rU') as f:
	    reader=csv.reader(f,delimiter='\t')
	    names = []
	    for student in reader:
	    	arr = shlex.split(student[0])
	    	stu = ""
	    	for i in arr[::-1]:
	    		stu += i
	    		stu += " "
	    	names.append((stu,student[3]))
	names.sort()
	#print names
	for name in names:
		g.write(name[0] + "\t" + name[1] + "\n")
	g.close()

alpha("W3")
alpha("W7")
alpha("Th9")
alpha("Th11")
alpha("Th1")
alpha("Th3")
alpha("Th5")
