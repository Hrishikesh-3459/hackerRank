def timeInWords(h, m):
    # I could have done this taking only one list, but for convenience and readability I have used 2 lists
    hours = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'tweleve'}
    minutes = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'tweleve',
                13: 'thirteen', 14 : 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one',
                22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
                29: 'twenty nine'}

    
    if (m == 00):
        return (f"{hours[h]} o' clock")
    elif (m <= 30):
        if (m == 1):
            return (f"{minutes[m]} minute past {hours[h]}")
        elif (m == 15):
            return (f"quarter past {hours[h]}")
        elif (m == 30):
            return (f"half past {hours[h]}")
        else : 
            return (f"{minutes[m]} minutes past {hours[h]}")
    elif (m > 30):
        if (m == 45):
            return (f"quarter to {hours[h+1]}")
        elif (60 - m == 1):
            return (f"{minutes[60-m]} minute to {hours[h+1]}")
        else :
            return (f"{minutes[60-m]} minutes to {hours[h+1]}")

        
print(timeInWords(3,00))