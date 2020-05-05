def taumBday(b, w, bc, wc, z):
    if (bc == wc):
        return (b * bc + w * wc)
    if (z > bc and z > wc):
        return (b * bc + w * wc)
    if (bc > wc + z):
        return(b * (wc + z) + w * wc)
    if (wc > bc + z):
        return(w * (bc + z) + b * bc)
    else:
        return (b * bc + w * wc)