#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

#if name == "__main__":
if __name__ == '__main__':
    for row in sys.stdin:
        data = row.strip().split("\t")
        letters = data[0]
        values = data[1]
    
        sys.stdout.write(f"{letters}\t{values}\n")

    

    

