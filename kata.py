def Add(number):
    if len(number) == 1:
        return int(number)

    elif len(number) == 3:
        num1, num2 = number.split(",")
        return int(num1) + int(num2)
        
    else:
        return 0