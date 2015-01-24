from PyPDF2 import PdfFileMerger, PdfFileReader

merger = PdfFileMerger()
filenames = ["W4.pdf", "W7.pdf", "Th9.pdf", "Th11.pdf", "Th1.pdf", "Th3.pdf", "Th5.pdf"]
for filename in filenames:
    merger.append(PdfFileReader(file("rosters/roster." + filename, 'rb')))

merger.write("rosters/seatingCharts.pdf")