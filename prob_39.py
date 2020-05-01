import math

def encryption(s):
    lim = math.sqrt(len(s))
    count = 0
    ans = ""
    while (count < math.ceil(lim)):
        for i in range(count,len(s),math.ceil(lim)):
            ans += s[i]
        ans += " "
        count += 1
    return(ans)

print(encryption("chillout"))
    
