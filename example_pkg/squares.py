#!/usr/bin/python3
# A Simple but useless program

class Squares(object):
    """docstring for Squares."""

    def __init__(self):
        super(Squares, self).__init__()
        print("This program simply squares a number provided by the user.")
        print("I hope you see this message")
        self.main_loop()

    def main_loop(self):
        # Setup the infinite user loop
        while (True):
            n = input("What number would you like to square today? (q to quit) ")
            # Catch 'q to quit'
            if 'q' in n:
                break
            # attempt to calculate square and print results.
            self.squares(n)
            print(self.s)
        return 0


    def squares(self, n):
        try:
            n = float(n)
        except:
            self.s="The value provided must be a number"
            return
        # If n can be an number, square it.
        self.s = n*n
