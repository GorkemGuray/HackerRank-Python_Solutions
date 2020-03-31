# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    len_s=len(string)
    len_ss=len(sub_string)
    number = 0

    for i in range (len_s):
        if (string[i:(i+len_ss)]==sub_string):
            number = number+1
    return number

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)