#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from operator import itemgetter
import pandas as pd

for line in sys.stdin:
    line = line.strip()
    letter, val, dates, = line.split('\t')
    val= int(val)
    df= pd.DataFrame([letter], [val], [dates])
    df=df.sort_values(['val'], ascending=True)
    #vals=int(val)
    #v=vals.sort()
    #sorted(val, key=itemgetter(1))
    print ('%s\t%s\t%s'% (letter, dates, val))

 