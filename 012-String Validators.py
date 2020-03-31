# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = str(input())

    isAlnum=False
    isAlpha=False
    isDigit=False
    isLower=False
    isUpper=False

    for i in s:
        if (i.isalnum()==True):
            isAlnum=True
            break
    
    for i in s:
        if (i.isalpha()==True):
            isAlpha=True
            break

    for i in s:
        if (i.isdigit()==True):
            isDigit=True
            break

    for i in s:
        if (i.islower()==True):
            isLower=True
            break

    for i in s:
        if (i.isupper()==True):
            isUpper=True
            break

    print(isAlnum)
    print(isAlpha)
    print(isDigit)
    print(isLower)
    print(isUpper)
    



    
    


    