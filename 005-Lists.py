# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    n = int(input())
    real_list = []

    for _ in range(n):
        command, *values = input().split()
        values_list = list(map(int,values))
        
        if (command == 'insert'):
            real_list.insert(values_list[0], values_list[1])
        
        if (command == 'print'):
            print(real_list)

        if (command == 'remove'):
            real_list.remove(values_list[0])

        if (command == 'append'):
            real_list.append(values_list[0])
        
        if (command == 'sort'):
            real_list.sort()

        if (command == 'pop'):
            real_list.pop()

        if (command == 'reverse'):
            real_list.reverse()



   