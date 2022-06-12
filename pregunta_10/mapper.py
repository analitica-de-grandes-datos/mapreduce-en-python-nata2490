#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

lista=[]
for line in sys.stdin:
    data = line.strip().split('\t')
    (key, val) = (data[0], data[1].strip().split(','))
    #print ("%s %s" % (k, v))
    for v in val:
    #    lista.append(list(datos[k]+datos[1][v]))
        print ("%s %s" % (k, v))

    

    

