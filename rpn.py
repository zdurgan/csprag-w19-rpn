#!/usr/bin/env python3

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}


def calculate(arg):
    stack = []
    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            function = operators[token]
            val2 = stack.pop()
            val1 = stack.pop()
            result = function(val1, val2)
            stack.append(result)

    if len(stack) > 1:
        raise ValueError("Too many arguments")
    return stack[-1]


def main():
    while True:
        try:
            result = calculate(input("rpn calc> "))
            print(result)
        except ValueError:
            pass


if __name__ == '__main__':
    main()