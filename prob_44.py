from collections import Counter

def appendAndDelete(s, t, k):
    tot_len = (len(s) + len(t))
    if(s == t):
        return ('Yes')
    dict1 = Counter(s) 
    dict2 = Counter(t)
    commonDict = dict1 & dict2 
    commonChars = set(commonDict.elements())
    print(commonChars)
    tot_len -= (len(commonChars) *2)
    print(tot_len)
    if((tot_len % k) == 0):
        return ('Yes')

    return('No')

print(appendAndDelete('ashley', 'ash', 2))