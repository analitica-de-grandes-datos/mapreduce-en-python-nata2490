#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from operator import itemgetter
import pandas as pd

#for line in sys.stdin:
    #val = line.strip().split()
    #(letters, dates,values)=(val[0], val[1], val[2])
    #line = line.strip()
    #data= line.split('\n')
    #val= int(val)
    #df= pd.DataFrame([letter], [val], [dates])
    #df=df.sort_values(['val'], ascending=True)
    #vals=int(val)
    #v=vals.sort()
    #sorted(val, key=itemgetter(1))
    #print ('%s\t%s\t%s'% (letter, dates, val))

 
my_list = {}

for line in sys.stdin:
    line = line.strip()
    letter, dates, value = line.split('\t')

    if letter in my_list:
        my_list[letter].append(float(value))
    else:
        my_list[letter] = []
        my_list[letter].append(float(value))

for letter in my_list.keys():
    max_letter = max(my_list[letter])
    min_letter = min(my_list[letter])
    print ('%s\t%s\t%s'% (letter, max_letter, min_letter))

 