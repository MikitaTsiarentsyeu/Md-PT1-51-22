while True:
    try:
        length = int(input("Enter string length value:\n")) + 1
        if length <= 35:
            raise Exception
        break
    except Exception:
        print("Error value. Enter correct value!")
curr_index = 0

with open("text.txt", 'r', encoding='utf-8') as f:
    with open("text_res.txt", 'w') as ff:
        total_iter_counter = 0
        while True:
            total_iter_counter += 1
            flag = True
            additional_index = 0
            additional_index_2 = 0
            s_counter = 0

            f.seek(curr_index)
            if f.read(1) == " ":
                temp_string = f.read(length)
                curr_index += 1
            else:
                f.seek(curr_index)
                temp_string = f.read(length)

            f.seek(curr_index)
            temp_string = f.read(length)
            end_index = length

            if not temp_string:
                break

            if "\n" in temp_string:
                end_index = temp_string.find("\n")
                additional_index += 2
                flag = False
            elif len(temp_string) >= 1 and temp_string[-1] == " ":
                end_index = length - 1
            elif len(temp_string) <= length - 1:
                flag = False
            else:
                end_index = temp_string.rindex(" ")

            curr_index += end_index + additional_index
            temp_string = temp_string[0:end_index]

            s_counter = length - 1 - end_index + additional_index_2
            while flag:
                for i in range(len(temp_string)-1, -1, -1):
                    if s_counter == 0:
                        flag = False
                        break
                    elif temp_string[i] == " ":
                        s_counter -= 1
                        temp_string = temp_string[:i+1] + temp_string[i:]

            print(temp_string)
            ff.write("\n" + temp_string) if total_iter_counter != 1 else ff.write(temp_string)

print("\nThe text was successfully saved to a file 'text_res.txt'.")
