def jumpingOnClouds(c):
    jump = 0
    pos = 0
    while ((pos + 2) <= len(c)):
        if (pos == len(c)-2):
            jump += 1
            pos += 1
            break
        if (c[pos+2] == 1):
            jump += 1
            pos += 1
        else:
            jump += 1
            pos += 2