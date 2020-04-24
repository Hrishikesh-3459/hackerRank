def bonAppetit(bill, k, b):
    total = (sum(bill) - bill[k]) / 2
    # Calculating the total, excluding 'k'
    if(total == b):
        # If the total matches we print bon appetit
        print("Bon Appetit")
    else:
        # If the total doesn't match we print the difference
        print(int(b - total))

bonAppetit([3,10,2,9], 1, 12)
