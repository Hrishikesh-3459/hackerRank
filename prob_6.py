def staircase(n):
    for i in range(n):
        for j in range(n,i+1,-1):
            print(" ", end="")
        for q in range(i+1):
            print("*", end = "")
        print()

staircase(1)