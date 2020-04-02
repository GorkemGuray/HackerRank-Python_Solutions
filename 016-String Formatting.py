# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):

    for i in range(1,number+1):

        print("{}".format(i).rjust(len(bin(number))-2), 
        "{}".format(oct(i).lstrip("0o")).rjust(len(bin(number))-2), 
        "{}".format(hex(i).lstrip("0x")).rjust(len(bin(number))-2).upper(),
        "{}".format(bin(i).lstrip("0b")).rjust(len(bin(number))-2), 
        )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)