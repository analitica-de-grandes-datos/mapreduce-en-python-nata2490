#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from itertools import groupby
from operator import itemgetter

def read_stdin_generator(data):
    for record in data:
        yield record.rstrip().split('\t')

def main():
    data= read_stdin_generator(sys.stdin)
    for month, group in groupby(data, itemgetter(0)):
        months= sum(int(count) for month, count in group)
        print('%s %d' % (month, months))

if __name__ == '__main__':
    main()

