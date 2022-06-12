#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#


import sys

my_list = {}

for line in sys.stdin:
    line = line.strip()
    letter, value = line.split('\t')

    if letter in my_list:
        my_list[letter].append(float(value))
    else:
        my_list[letter] = []
        my_list[letter].append(float(value))

for letter in my_list.keys():
    max_letter = max(my_list[letter])
    min_letter = min(my_list[letter])
    print ('%s\t%s\t%s'% (letter, max_letter, min_letter))

        
