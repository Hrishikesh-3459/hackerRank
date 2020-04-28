def formingMagicSquare(s):
    cord = []
    col_sum = [0,0,0]
    sum_dia = 0
    # Add another diagonal
    for i in range(len(s)):
        col_sum[0] += s[i][0]
        col_sum[1] += s[i][1]
        col_sum[2] += s[i][2]
        sum_dia += s[i][i]
    row_sum = [sum(s[0]), sum(s[1]), sum(s[2])]
    # col_sum = [sum_col_1, sum_col_2, sum_col_3]
    # i = 0
    for i in range(len(s)):
        if(row_sum[i] != 15):
            diff = 15 - row_sum[i]
            cord.append(i)
        if(col_sum[i] != 15):
            diff = 15 - col_sum[i]
            cord.append(i)
        
    s[cord[0]][cord[1]] += diff
    print(cord)
    print(s)



formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]])
