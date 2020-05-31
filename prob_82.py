# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stack = [0]
for i in range(n):
    y = list(map(int, input().split()))
    if (y[0] == 1):
        stack.append(max(y[1], stack[-1]))
    elif(y[0] == 2):
        stack.pop()
    elif(y[0] == 3):
        print(stack[-1])
