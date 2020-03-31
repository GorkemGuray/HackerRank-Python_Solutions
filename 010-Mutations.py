# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    liste = list(string)
    liste[position] = character
    new = ''.join(liste)
    return new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)