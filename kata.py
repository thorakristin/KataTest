def Add(number):
    if number is "":
        return 0

    number_in_list = number.split(",")
    number_in_list = [int(i) for i in number_in_list]

    return sum(number_in_list)