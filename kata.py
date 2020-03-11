def Add(number):
    if number is "":
        return 0

    number = number.replace("\n",",")
    number_in_list = number.split(",")
    number_in_list = [int(i) for i in number_in_list]

    return sum(number_in_list)