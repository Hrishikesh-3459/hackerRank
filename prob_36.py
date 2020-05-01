def permutationEquation(p):
    ans = []
    for i in range(len(p)):
        y = p.index(i+1)
        ans.append(p.index(y+1)+1)

    return(ans)

print(permutationEquation([4,3,5,1,2]))


