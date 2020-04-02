# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# 4*size-3 : according to size, number of element on the line

def num2alpha(num):
    base=96
    return (chr(base+num))

def generator(start,stop):
    x = []
    for i in range(stop,start,-1):
        x.append(num2alpha(i)+"-")
    for i in range(start,stop+1):
        if(i!=stop):
            x.append(num2alpha(i)+"-")
        else:
            x.append(num2alpha(i))
    
    return x


def print_rangoli(size):
    
    # upside (include middle)
    for i in range(size, 0, -1):
        x = generator(i,size)
        print(''.join(x).center(4*size-3,"-"))

    # downside
    for i in range(2, size+1):
        x = generator(i,size)
        print(''.join(x).center(4*size-3,"-"))


if __name__ == '__main__':
    n = int(input())


    print_rangoli(n)
