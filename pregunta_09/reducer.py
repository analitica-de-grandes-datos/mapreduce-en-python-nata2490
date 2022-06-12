#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

my_list = {}

for line in sys.stdin:
    line = line.strip()
    values, letters, dates = line.split('\t')

    if letters in my_list:
        my_list[letters].append(int(values))
    else:
        my_list[letters] = []
        my_list[letters].append(int(values))

for letters in my_list.keys():
    sum_letter = sum(my_list[letters])
    print ('%s\t%s\t%s'% (letters, dates, values))
