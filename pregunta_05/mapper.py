#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def read_stdin_geneartor(file):
    for record in file:
        yield record
def main():
    data=read_stdin_geneartor(sys.stdin)
    for record in data:
        #year= record[4:8]
        month= record[9:11]
        #print('%s-%s\t%d' % (year, month, 1))
        print('%s\t%d' % (month, 1))

if __name__ == '__main__':
    main()