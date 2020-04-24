def sockMerchant(n, ar):
    colours = []
    pair = 0
    for i in range(n):
        if(ar[i] not in colours):
            colours.append(ar[i])
            print(colours)
        else:
            pair += 1
            colours.remove(ar[i])
            print(colours)
    return(pair)


print(sockMerchant(9, [10,20,20,10,10,30,50,10,20]))

# x = [10,20,20,10,10,30,50,10,20]
# x.pop()
# print(x)