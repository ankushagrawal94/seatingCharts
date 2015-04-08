from PyPDF2 import PdfFileMerger, PdfFileReader

merger = PdfFileMerger()
filenames = ["W4.pdf", "W6.pdf", "W8.pdf", "Th9.pdf", "Th11.pdf", "Th1.pdf", "Th3.pdf", "Th5.pdf", "Th7.pdf", "F10.pdf", "F12.pdf"]
for filename in filenames:
    merger.append(PdfFileReader(file("rosters/roster." + filename, 'rb')))

merger.write("rosters/seatingCharts.pdf")