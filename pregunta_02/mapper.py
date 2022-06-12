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
            amount = columns[3]
            purpose= columns[4]
            
            print ("%s\t%s" % (amount, purpose))
        except ValueError:
            pass
