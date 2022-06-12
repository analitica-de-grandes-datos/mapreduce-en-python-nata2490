#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    #line = line.strip()
    columns = line.split() # split line into parts
    # the data is messy, only read those having correct column count
    if len(columns) == 3: 
        try:
            column0 = columns[0]
            
            print ("%s\t%s" % (column0, 1))
        except ValueError:
            pass


