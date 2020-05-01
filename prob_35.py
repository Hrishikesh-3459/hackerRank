def cutTheSticks(arr):
    arr.sort()
    temp_list = []
    ans = []
    while True:
        for i in arr:
            count = 0
            temp_list.append(i - arr[count])
            count += 1
        ans.append(len(temp_list))
        if(temp_list[len(arr)-1] == 0):
            break
        temp_list.clear()
    return(ans)
print(cutTheSticks([5,4,4,2,2,8]))

        