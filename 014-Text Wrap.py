# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    string_wrapped_list = wrapper.wrap(string)
    string_wrapped = '\n'.join(string_wrapped_list)
    return string_wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)