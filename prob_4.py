def diagonalDifference(arr):
    prim_dia = 0
    seco_dia = 0
    count = len(arr)-1
    for i in range(len(arr)):
        prim_dia = prim_dia + arr[i][i]
    for q in range(len(arr)):
        seco_dia = seco_dia + arr[q][count]
        count -= 1
    return(abs(seco_dia - prim_dia))

