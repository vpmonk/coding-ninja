def nStarDiamond(n: int) -> None:
    # Upper part of the diamond
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    # Lower part of the diamond
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(2 * (n - i) - 1):
            print("*", end="")
        print()
