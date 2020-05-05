def acmTeam(topic):
    max_count = 0
    count = 0
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            temp_count = 0
            for k in range(len(topic[0])):
                if(topic[i][k] == '1' or topic[j][k] == '1'):
                    temp_count += 1
            if (temp_count > max_count):
                max_count = temp_count
                count = 0
            elif (temp_count == max_count):
                count += 1
    return([max_count, count+1])
acmTeam(['10101', '11100', '11010', '00101'])