
while True:
    length = input("Please enter the max amount of symbols (the value must be more than 35 symbols):\n")
    if length.isdigit() == False:
        print("String length must contain only number\n")
        continue
    if int(length) < 35:
        print("String length must be more than 35 symbols\n")
        continue
    break

length = int(length)

def align(str, length):
    list = str.split()
    counter = 0
    for list_elem in list:
        counter += len(list_elem)
    while counter < length:
        for list_index in range(len(list)-1):
            if counter < length:
                list[list_index] += " "
                counter += 1
            else:
                break   
    return "".join(list)



with open("text.txt", "r+", encoding='utf-8') as donor:
    with open("copied_text.txt", 'w+', encoding='utf-8') as recipient:
        for line in donor:
            start_index = 0
            finish_index = start_index + length
            last_space = line.rindex(" ")
    while finish_index <= last_space:
        if len(line) - finish_index > length:
            finish_index = line.rindex(" ", start_index, start_index + length)
            str = line[start_index:finish_index].strip()
            recipient.write(align(str, length) + "\n")
            start_index += len(line[start_index:finish_index]) 
        else:
            recipient.write(line[finish_index:].strip() + '\n')
            break
print("Everything is working. Edited file is saved in copied_text.txt")        