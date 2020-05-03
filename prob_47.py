import math
def repeatedString(s, n):
    a = s.count('a')
    ans = math.ceil((a*n) / len(s))
    return(ans)



print(repeatedString('a',1000000000000))