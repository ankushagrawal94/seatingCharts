import csv, random, sys, math
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

#globals
allStudents = []

def importStudents():
    with open('/Development/seatingCharts/' + sys.argv[1],'rU') as f:
        reader=csv.reader(f,delimiter='\t')
        for student in reader:
            allStudents.append(student[0] + '\t' + student[3])
    print(allStudents)

def hello(c):
    c.drawString(100,100,"Hello World")

def row(c):
    c.drawString(100, 100, "Hello")

def title(c):
    c.setFont("Helvetica", 24)
    c.drawString(5.5*inch, -1.4*inch, "Wed 1PM")
    c.drawString(5.75*inch, -1.0*inch, "Lab 2")
    c.drawString(5.5*inch, -0.6*inch, "CSE 15L")

def rows(c):
    c.setStrokeColorRGB(1, 0, 0)
    c.rect(.65*inch, -2.5*inch, 10.5*inch, 1*inch, stroke = 1)
    c.setStrokeColorRGB(0, .75, 0)
    c.rect(.65*inch, -5.85*inch, 10.5*inch, 1.75*inch, stroke = 1)

def fillOdd(c):
    c.setFont("Helvetica", 9)
    xStart = -.1*inch
    yStart = -.75*inch
    yInc = 1*inch
    xInc = 1*inch
    yGap = -.3*inch
    xGap = 1.125*inch
    name = "Test, Name"
    seat = 1
    cseat = 1
    count = -1
    for i in range(7):
        k = 0
        for k in range(6):
            if ( i*k > len(allStudents)):
                return
            count = count + 1
            stu = allStudents[count]
            stuArr = stu.split("\t")
            name = stuArr[0]
            seat = stuArr[1]
            if( (seat > 6  and seat < 13) or (seat > 18 and seat < 25) or (seat > 30 and seat < 37) ):
                k = k-1
                #print(k)
                cseat = cseat + 1
                seat = seat +1
                continue
            print("seat: %s", seat)
            q = (int(math.floor(cseat)) -1 if int(math.floor(cseat)) %2 == 0  else int(math.floor(cseat)))
            print( q)
            if(int(seat) !=  q):
                seat = int(math.floor(cseat))
                name = "NO NAME"
                # change index of number - 1
            else:
                if((math.floor(cseat)) %2 == 0):
                    c.drawString(xStart + xInc, yStart - yInc, name)
                    c.drawString(xStart + xInc + xGap, yStart-yInc , str(seat))

                else:
                    c.drawString(xStart + xInc, yStart - yInc + yGap, name)
                    c.drawString(xStart + xInc + xGap, yStart-yInc+yGap , str(seat))
                    xInc = xInc + 1.625*inch
            cseat = cseat + 1

            print(seat)
        if( i%2 == 1):
            xInc = 1*inch
            yInc = yInc + 1.75*inch

importStudents()
c = canvas.Canvas("hello.pdf")
c.translate(0*inch, 0*inch)
c.rotate(90)
c.rect(.65*inch,-7.5*inch,10.5*inch,6*inch, stroke=1)
title(c)
rows(c)
#fillOdd(c)
c.setFillColorRGB(20, 35, 33)
c.showPage()
c.save()
