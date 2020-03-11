def Add(number):
    if number is "":
        return 0

    number = number.replace("\n",",")
    number_in_list = number.split(",")
    number_in_list = [int(i) for i in number_in_list]

    new_list = []
    for i in number_in_list:
        if i <= 1000:
            new_list.append(i)

    return sum(new_list)