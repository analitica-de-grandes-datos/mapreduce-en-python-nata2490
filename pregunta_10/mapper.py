#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    for line in sys.stdin:
        data = line.strip().split("\t")
        letters = data[0]
        values = data[1]
    
        sys.stdout.write(f"{letters}\t{values}\n")

    

    

