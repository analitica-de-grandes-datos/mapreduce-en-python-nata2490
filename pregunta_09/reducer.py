#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import pandas as pd

for line in sys.stdin:
    line = line.strip()
    letters, dates, values, = line.split('\t')
    value=int(values)
    df= pd.DataFrame({letters, dates, value})
    dff=df.sort_values(by= 'values', ascending=True)
    print ('%s\t%s\t%s'% (letters, dates, dff))
