import csv, random, sys, math
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

#globals
allStudents = []
occupied = [0] * 100

def importStudents():
    with open('/Development/seatingCharts/' + sys.argv[1],'rU') as f:
        reader=csv.reader(f,delimiter='\t')
        for student in reader:
            allStudents.append(student[0] + '\t' + student[3])

def hello(c):
    c.drawString(100,100,"Hello World")

def row(c):
    c.drawString(100, 100, "Hello")

def title(c):
    c.setFont("Helvetica", 24)
    c.drawString(5.8*inch, -1.4*inch, sys.argv[1][sys.argv[1].index(".")+1:])
    c.drawString(5.5*inch, -1.0*inch, "CSE 15L")

def rows(c):
    #c.setStrokeColorRGB(1, 0, 0)
    c.rect(.65*inch, -2.5*inch, 10.5*inch, 1*inch, stroke = 1)
    #c.setStrokeColorRGB(0, .75, 0)
    c.rect(.65*inch, -5.85*inch, 10.5*inch, 1.75*inch, stroke = 1)

def printRow(c):
    c.setFont("Helvetica", 10)
    c.line(2.45*inch,-7.5*inch,2.45*inch, -1.5*inch)
    c.line(4.15*inch,-7.5*inch,4.15*inch, -1.5*inch)
    c.line(5.85*inch,-7.5*inch,5.85*inch, -1.5*inch)
    c.line(7.55*inch,-7.5*inch,7.55*inch, -1.5*inch)
    c.line(9.25*inch,-7.5*inch,9.25*inch, -1.5*inch)

    for stu in allStudents:
        stuArr = stu.split("\t")
        name = stuArr[0]
        seat = int(stuArr[1])
        if (occupied[seat] == 0):
            occupied[seat] = occupied[seat] + 1
            yOffset = 0
        else:
            #occupied at seat is 1 meaning someone already at that seat
            yOffset = -.4*inch
        ySeperator = -2.5*inch
        if seat == 1:
            c.drawString(.9*inch, -1.8*inch + yOffset, name)
            c.drawString(2.1*inch, -1.8*inch + yOffset, str(seat))
        if seat == 2:
            c.drawString(2.6*inch, -1.8*inch + yOffset, name)
            c.drawString(3.8*inch, -1.8*inch + yOffset, str(seat))
        if seat == 3:
            c.drawString(4.3*inch, -1.8*inch + yOffset, name)
            c.drawString(5.5*inch, -1.8*inch + yOffset, str(seat))
        if seat == 4:
            c.drawString(6.0*inch, -1.8*inch + yOffset, name)
            c.drawString(7.2*inch, -1.8*inch + yOffset, str(seat))
        if seat == 5:
            c.drawString(7.7*inch, -1.8*inch + yOffset, name)
            c.drawString(8.9*inch, -1.8*inch + yOffset, str(seat))
        if seat == 6:
            c.drawString(9.4*inch, -1.8*inch + yOffset, name)
            c.drawString(10.6*inch, -1.8*inch + yOffset, str(seat))

        ySeperator = -.9*inch

        if seat == 7:
            c.drawString(9.4*inch , -1.8*inch + yOffset + ySeperator, name)
            c.drawString(10.6*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 8:
            c.drawString(7.7*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(8.9*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 9:
            c.drawString(5.9*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(7.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 10:
            c.drawString(4.3*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(5.5*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 11:
            c.drawString(2.6*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(3.8*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 12:
            c.drawString(.9*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(2.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))
           
        ySeperator = -1.8*inch

        if seat == 13:
            c.drawString(.9*inch, -1.8*inch + yOffset  + ySeperator, name)
            c.drawString(2.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 14:
            c.drawString(2.6*inch, -1.8*inch + yOffset  + ySeperator, name)
            c.drawString(3.8*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 15:
            c.drawString(4.3*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(5.5*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 16:
            c.drawString(6.0*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(7.2*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 17:
            c.drawString(7.7*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(8.9*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 18:
            c.drawString(9.4*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(10.6*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        
        ySeperator = -2.7*inch
        
        if seat == 19:
            c.drawString(9.4*inch , -1.8*inch + yOffset + ySeperator, name)
            c.drawString(10.6*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 20:
            c.drawString(7.7*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(8.9*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 21:
            c.drawString(5.9*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(7.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 22:
            c.drawString(4.3*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(5.5*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 23:
            c.drawString(2.6*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(3.8*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 24:
            c.drawString(.9*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(2.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))

        ySeperator = -3.5*inch

        if seat == 25:
            c.drawString(.9*inch, -1.8*inch + yOffset  + ySeperator, name)
            c.drawString(2.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 26:
            c.drawString(2.6*inch, -1.8*inch + yOffset  + ySeperator, name)
            c.drawString(3.8*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 27:
            c.drawString(4.3*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(5.5*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 28:
            c.drawString(6.0*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(7.2*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 29:
            c.drawString(7.7*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(8.9*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 30:
            c.drawString(9.4*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(10.6*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        
        ySeperator = -4.4*inch
        
        if seat == 31:
            c.drawString(9.4*inch , -1.8*inch + yOffset + ySeperator, name)
            c.drawString(10.6*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 32:
            c.drawString(7.7*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(8.9*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 33:
            c.drawString(5.9*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(7.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 34:
            c.drawString(4.3*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(5.5*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 35:
            c.drawString(2.6*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(3.8*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 36:
            c.drawString(.9*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(2.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))

        ySeperator = -5.2*inch

        if seat == 37:
            c.drawString(.9*inch, -1.8*inch + yOffset  + ySeperator, name)
            c.drawString(2.1*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 38:
            c.drawString(2.6*inch, -1.8*inch + yOffset  + ySeperator, name)
            c.drawString(3.8*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 39:
            c.drawString(4.3*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(5.5*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 40:
            c.drawString(6.0*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(7.2*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 41:
            c.drawString(7.7*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(8.9*inch, -1.8*inch + yOffset + ySeperator, str(seat))
        if seat == 42:
            c.drawString(9.4*inch, -1.8*inch + yOffset + ySeperator, name)
            c.drawString(10.6*inch, -1.8*inch + yOffset + ySeperator, str(seat))
           
importStudents()
c = canvas.Canvas(sys.argv[1]+".pdf")
c.translate(0*inch, 0*inch)
c.rotate(90)
c.rect(.65*inch,-7.5*inch,10.5*inch,6*inch, stroke=1)
title(c)
rows(c)
printRow(c)
#fillOdd(c)
c.setFillColorRGB(20, 35, 33)
c.showPage()
c.save()
