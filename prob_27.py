def hurdleRace(k, height):
    if(k > max(height)):
        return(0)
    else:
        return(abs(max(height) - k))