# https://www.hackerrank.com/challenges/designer-door-mat/problem

if __name__ == '__main__':
    n,m = input().split()
    n = int(n)
    m = int(m)

    half_n = int((n-1)/2)
    
    #upper side
    for i in range (1,half_n+1):
        if (i!=1):
            s = (i*2)-1
        else:
            s=1

        #print("-"*int((m-3*s)/2) + ".|."*(s) + "-"*int((m-3*s)/2))
        print((".|."*s).center(m,"-"))

    #middle
    print("WELCOME".center(m,"-"))

    #bottom side
    for i in range (half_n,0,-1):
        if (i!=1):
            s = (i*2)-1
        else:
            s=1

        print((".|."*s).center(m,"-"))

    



    




