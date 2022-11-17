import os

text_folder = os.path.dirname(__file__)
text_file = text_folder.replace("Liavonchyk/Task4","!Tasks/Task4/text.txt") # get path to the initial file
char_amount_num = 0

while char_amount_num < 35 :
    char_amount = input("Please enter the amount of symbols >=35: \n")
    if char_amount.isdigit():
        char_amount_num = int(char_amount) - 1 # to have \n as the 40th symbol

text = []
ending_list = [" ","\n"]
j = 0
i = 0

with open(text_file, 'r') as from_read:
    with open("new_text.txt", 'w') as to_write:
        while True:
            line = from_read.readline() # we will process file line by line
            line_len = len(line)
            i = 0
            j = 0
            text = []
            while i < line_len:
                if line_len > i + char_amount_num:
                    if line[i + char_amount_num] in ending_list : # we get exact part of text
                        text.append(line[i:i + char_amount_num])
                        i = i + char_amount_num + 1
                    elif line[i + char_amount_num] not in ending_list: # we need to do some magic
                        for j in range(i + char_amount_num - 1, i, -1):
                            if line[j] == " ":
                                differ = i + char_amount_num - j # counter how many spaces do we need to add
                                new_line = line[i:j]
                                space_count = {}
                                for count, value in enumerate(new_line): # get indices of spaces
                                    if value == " ":
                                        space_count[count] = " "

                                while differ > 0: # prepare the dict that will be used to replace one with many spaces by index.
                                    for key in space_count.keys():
                                        if differ > 0:
                                            space_count[key] = space_count[key] + " "
                                            differ = differ - 1
                                        else:
                                            pass

                                for k in range(len(new_line) - 1, 0, -1): # Replace spaces by index
                                    if k in space_count.keys() and new_line[k] == " ":
                                        new_line = new_line[:k] + space_count[k] + new_line[k + 1:]

                                text.append(new_line)
                                i = j + 1
                                break
                else: # we get the end of the line and will add it as it is
                    text.append(line[i:line_len])
                    i = line_len

            if line:
                for k in text:
                    k = k.replace("\n","")
                    to_write.write(k)
                    to_write.write("\n")
            else:
                print("Job's done!")
                break

with open("new_text.txt", 'rb+') as filefix: # remove last added \n
    filefix.seek(-1, os.SEEK_END)
    filefix.truncate()

