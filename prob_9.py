def timeConversion(s):
    out = s
    if(s[-2] == 'A' and s[:2] == '12'):
        out = s.replace('12', '00', 1)
    if(s[-2] == 'P' and s[:2] != '12'):
        x = str(int(s[:2]) + 12)
        out = s.replace(s[:2], x, 1)

    return(out[:-2])
print(timeConversion("03:50:00PM"))
