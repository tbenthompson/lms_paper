from os import listdir, system
from os.path import isfile, join

directory = './'
for f in listdir(directory):
    if not isfile(join(directory, f)):
        continue
    if not f.lower().endswith('.pdf'):
        continue
    system('pdfcrop ' + f + ' ' + f)
