def pickingNumbers(a):
    nums = [[a[i] for i in range(len(a))] for j in range(len(a))] 
    for i in range(len(a)):
        temp_num = min(nums[i])
        for j in nums[i]:
            diff = abs(temp_num - j)
            if(diff > 1):
                nums[i].pop(nums[i].index(j))
    return(len(nums[0]))    

        
     
            

print(pickingNumbers([1,2,2,3,1,2]))