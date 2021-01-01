#!/usr/bin/python3
# A Simple but useless program
import numpy

def squares(n):
    try:
        n = float(n)
    except:
        e="The value provided must be a number"
        return e
    # If n can be an number, square it.
    s = n*n
    return s


if __name__ == '__main__':
    print("This program simply squares a number provided by the user.")
    print("I hope you see this message")
    # Setup the infinite user loop
    while (True):
        n = input("What number would you like to square today? (q to quit) ")
        # Catch 'q to quit'
        if 'q' in n:
            break
        # attempt to calculate square and print results.
        s = squares(n)
        print(s)
