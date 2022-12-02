import os, platform

def justify_text_for_limit(buffer: str, limit: int):
    buffer = buffer.strip()

    if len(buffer) == limit:
        return buffer

    elif len(buffer) > limit:
        return 'Your parameter must be < than parameter "limit".'

    else:

        if buffer[len(buffer) - 1] == "." or buffer[len(buffer) - 1] == "!" or buffer[len(buffer) - 1] == "?":
            return buffer
        else:
            string_is_done = ""
            str1, str3 = "", ""
            while len(string_is_done + buffer) < limit:
                if " " not in buffer:
                    buffer = temp
                    string_is_done = ""

                str1, str3 = buffer.partition(" ")[0], buffer.partition(" ")[2]
                temp = string_is_done + str1 + "  " + str3

                if len(temp) < limit:
                    string_is_done = string_is_done + str1 + "  "
                    buffer = str3
                    continue
                else:

                    buffer = temp
                    return buffer

while True:
    user_input = input('Program for justify text into file "text.txt". Input your maximum length of string.\nType limit (input integer number >= 35):\n')
    if int(user_input) < 35:
        print("Length of string is too short...\n")
        continue
    break

os.chdir(os.path.dirname(os.path.abspath(__file__)))

limit = int(user_input)
line_counter = sum(1 for line in open("text.txt"))

fc = open("text_out.txt", "w")
fc.close

with open("text.txt", "r+", encoding="utf-8") as fr:

    for line in fr:
        data = line.split(' ')
        buffer = ''

        while data != []:
            
            i = 0
            while len(buffer.strip()) + len(data[0]) < limit:
                buffer = buffer + data[0] + ' '
                del(data[0])
                if data == []:
                    break
                i += 1
            else:

                buffer = buffer.strip()

                write_buff = justify_text_for_limit(buffer, limit) + "\n"

                with open("text_out.txt", "a+", encoding="utf-8") as fw:
                    fw.writelines(write_buff)

                buffer = ""
                i += 1
        else:

            if data == []:
                buffer = buffer.strip()
                write_buff = justify_text_for_limit(buffer, limit) + "\n"
                with open("text_out.txt", "a+", encoding="utf-8") as fw:
                    fw.writelines(write_buff)

print('\nFile "text_out.txt" is done. Check result, please, and close file...')

if platform.system() == "Windows" or platform.system() == "win32":
    os.system('notepad.exe text_out.txt')
if platform.system() == "Linux":
    os.system('nano text_out.txt')