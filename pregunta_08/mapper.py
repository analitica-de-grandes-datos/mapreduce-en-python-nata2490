#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    val = line.strip().split()
    (letters, values)=(val[0], val[2])
    print('%s\t%s' % (letters, values))

