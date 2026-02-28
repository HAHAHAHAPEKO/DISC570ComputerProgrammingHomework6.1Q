def digit():
    x = int(input("Enter a whole positive number: "))
    if len(str(x)) != 4:
        return print("Bad because not 4 digits.")

    elif x%10 == 0:
        return print("Bad because end with a 0.")

    elif x%2 != 0:
        return print("Not a EVEN number.")

    else:
        return print("Thanks.")

digit()
