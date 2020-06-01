# Enter your code here. Read input from STDIN. Print output to STDOUT
s = ""
str_op = []
for i in range(int(input())):
    x = input().split()
    if (x[0] == '1'):
        s += x[1]
        str_op.append(s)
    if (x[0] == '3'):
        pos = int(x[1]) - 1
        print(s[pos])
    if (x[0] == '2'):
        s = s[ : len(s) - int(x[1])]
        str_op.append(s)
    if (x[0] == '4'):
        str_op.pop()
        if (str_op):
            s = str_op[-1]  
        else:
            s = ""
