def climbingLeaderboard(scores, alice):
    x = set(scores)
    y = list(sorted(x, reverse=True))
    print(y)
    flag = False
    rank_alice = []
    for i in alice:
        for j in scores:
            if (i >= j):
                flag = True
                rank_alice.append(y.index(j)+1)
                break
        if(flag == False):
            flag = True
            rank_alice.append(len(y)+1)
            
            

    print(rank_alice)

    


print(climbingLeaderboard([100,90,90,80,75,60], [50,65,77,90,102]))