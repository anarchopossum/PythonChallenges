def decode(message_file):
    word_list = []
    for line in message_file.readlines():
        line_list = line.split()
        line_list[0] = int(line_list[0])
        word_list.append(line_list)
    # sorts lists based off x[0] in word list.
    word_list.sort(key=lambda x: x[0])

    ret_str = ''
    count = 1
    temp_list = []
    for list in word_list:
        if len(temp_list) >= count:
            ret_str += (f"{temp_list[:1][0]} ")
            count += 1
            temp_list = []
            temp_list.append(list[1])

        elif len(temp_list) < count:
            temp_list.append(list[1])
            if list is word_list[-1]:
                ret_str += (f"{list[1]}")

    return ret_str
        
with open('coding_qual_input.txt') as file:
    print(decode(file))
