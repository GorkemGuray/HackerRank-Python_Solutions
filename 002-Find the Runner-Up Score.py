# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) # Boşlukla yazılan girişleri listeye alıyor.


    arr.sort(reverse=True)

    isFound=False
    k = 0

    while (isFound == False):
        if arr[k] == arr[k+1]:
            isFound = False
            k = k+1
        else :
            print(arr[k+1])
            isFound = True

    

