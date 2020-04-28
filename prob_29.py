def utopianTree(n):
    tree = 1
    flag = True
    for i in range(n):
        if(flag == True):
            tree = tree * 2
            flag = False
        elif(flag == False):
            tree = tree + 1
            flag = True

    return(tree)

print(utopianTree(5))