def migratoryBirds(arr):
    max_count = 0
    ans = 0
    for i in arr:
        temp_count = arr.count(i)
        if(temp_count > max_count):
            max_count = temp_count
            ans = i
        elif((temp_count == max_count) and (ans > i)):
            ans = i
    return(ans)

print(migratoryBirds([2,2,1,1]))

# Taking a long time to run, hence two input tests are not completed

# count = [0]*6
#     for t in arr:
#         count[t] += 1
#     return((count.index(max(count))))

# This is the submitted answer