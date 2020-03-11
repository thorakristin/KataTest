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

    negative_str = ""
    for i in new_list:
        if i < 0:
            negative_str += str(i)
            negative_str += ","
    negative_str.strip(",")

    if len(negative_str) > 0:
        raise ValueError("Negatives not allowed:"+negative_str)

    return sum(new_list)