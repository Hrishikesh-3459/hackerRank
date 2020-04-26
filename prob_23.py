def getMoneySpent(keyboards, drives, b):
    spent = 0
    for i in keyboards:
        for j in drives:
            temp_spent = i + j
            if(temp_spent > spent and temp_spent <= b):
                spent = temp_spent

    if(spent == 0):
        return(-1)

    return(spent)


print(getMoneySpent([3,4], [5,2,8], 11))
