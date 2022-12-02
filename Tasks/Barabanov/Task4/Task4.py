while True:
    try:
        length = int(input("Enter string length value:\n")) + 1
        if length <= 35:
            raise Exception
        break
    except Exception:
        print("Error value. Enter correct value!")
curret_index = 0

with open("text.txt", "r", encoding="utf-8") as f:
    with open("text_pars.txt", "w") as ff:
        total_counter = 0
        while True:
            total_counter += 1
            flag = True
            add_index_1 = 0
            add_index_2 = 0
            str_counter = 0

            f.seek(curret_index)
            if f.read(1) == " ":
                buff_string = f.read(length)
                curret_index += 1
            else:
                f.seek(curret_index)
                buff_string = f.read(length)

            f.seek(curret_index)
            buff_string = f.read(length)
            end_index = length

            if not buff_string:
                break

            if "\n" in buff_string:
                end_index = buff_string.find("\n")
                add_index_1 += 2
                flag = False
            elif len(buff_string) >= 1 and buff_string[-1] == " ":
                end_index = length - 1
            elif len(buff_string) <= length - 1:
                flag = False
            else:
                end_index = buff_string.rindex(" ")

            curret_index += end_index + add_index_1
            buff_string = buff_string[0:end_index]

            str_counter = length - 1 - end_index + add_index_2
            while flag:
                for i in range(len(buff_string) - 1, -1, -1):
                    if str_counter == 0:
                        flag = False
                        break
                    elif buff_string[i] == " ":
                        str_counter -= 1
                        buff_string = buff_string[: i + 1] + buff_string[i:]

            print(buff_string)
            ff.write("\n" + buff_string) if total_counter != 1 else ff.write(
                buff_string
            )

print("\nThe text saved to a file 'text_pars.txt'.")
