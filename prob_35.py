def cutTheSticks(arr):
    new = arr[:]
    ans = [len(new)]
    nexta = []
    for i in range(len(arr)):
        small = min(new)
        for j in new:
            num = j - small
            if(num != 0):
                nexta.append(num)
        ans.append(len(nexta))
        new.clear()
        new.extend(nexta) 
        nexta.clear()
        if(len(new) == 0):
            break
    return(ans[0:len(ans)-1])

print(cutTheSticks([1,2,3,4,3,3,2,1]))

        