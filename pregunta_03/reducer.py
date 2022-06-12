#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

for line in sys.stdin:
    val = line.strip().split()
    (letters, values) = line.split()
    print ('%s,%s' % (values, letters)) 
