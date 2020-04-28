def pickingNumbers(a):
    temp_list = []
    for i in a:
        if(max(a) - i <= 1):
            temp_list.append(i)

    


print(pickingNumbers([1,2,2,3,1,2]))

