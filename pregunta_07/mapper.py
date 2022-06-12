#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

my_list = {}

for line in sys.stdin:
    line = line.strip()
    letter, dates, value = line.split('\t')

    if letter in my_list:
        my_list[letter].append(int(value))
    else:
        my_list[letter] = []
        my_list[letter].append(int(value))
        #print ('%s\t%s\t%s'% (letter, dates, val))
