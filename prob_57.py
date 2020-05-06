def camelcase(s):
    counter = 1
    for i in s:
        if (i.isupper()):
            counter += 1

    return(counter)