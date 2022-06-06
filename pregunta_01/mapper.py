#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts
    # the data is messy, only read those having correct column count
    if len(columns) == 21: 
        try:
            column3 = columns[2]
            #column3=sorted(column3)
            print ("%s\t%s" % (column3, 1))
        except ValueError:
            pass
       
