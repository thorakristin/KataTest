def Add(number):
    if number is "":
        return 0

    if number[0:2] == "//" and number[3] == "\n":
        delimeter = number[2]
        number = number[4:]
    else:
        delimeter = ","

    number = number.replace("\n",delimeter)
    number_in_list = number.split(delimeter)
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