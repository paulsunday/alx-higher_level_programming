#!/usr/bin/python3
"""nqueens backtracking programs to print the coordinates
of non-attacking position
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

        # initializing the answer list
    for i in range(n):
        a.append([i, None])


    def it_already_exists(y):
        """Checks that a queen does not already exist in the value y"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """It determines whether to reject the solution"""
        if it_already_exists(y):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
            return True

    def clear_a(x):
        """It clears the answers from the point of failure"""
        for c in range(x, n):
            a[c][1] == None

    def nqueens(x):
        """The recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):
                    print(a)
                else:
                    nqueens(x + 1)


    nqueens(0)
