#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from operator import itemgetter 
import sys

words = {}

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t')
    try:
        count = int(count)
        words[key] = words.get(key, 0) + count
    except ValueError:
        # ignore lines where the count is not a number
        pass

# sort alphabetically
sort_words = sorted(words.items(), key=itemgetter(0))

# output to STDOUT
for key, val in sort_words:
    print ('%s\t%s'% (key, val))



