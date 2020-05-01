def libraryFine(d1, m1, y1, d2, m2, y2):
    if (d2 >= d1 and m2 >= m1 and y2 >= y1):
        return(0)
    if (y1 != y2):
        return("10000")
    if (m1 != m2):
        return(500 * (m1 - m2))
    if (d1 != d2):
        return(15 * (d1 - d2))