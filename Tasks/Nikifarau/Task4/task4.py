def get_content():
    with open("text.txt", "r", encoding="utf-8") as donor:
        all_content = donor.read().replace("\n", " ").replace("  ", " ").replace("   ", " ").replace("’", "'").\
            replace("“", "\"").replace("”", "\"")
    return all_content


your_long = input("Enter the number of string long (> 35):\n")
while your_long.isdigit() is False or int(your_long) < 36:
    your_long = input("Your long is wrong, please, enter again (attention: a number must be > 35):\n")

your_long = int(your_long) - 1
all_content = get_content()
reading_index = 0
len_all_context = len(all_content)

with open("new_text2.txt", "w") as recepient:
    while reading_index < len_all_context:
        if len_all_context - reading_index >= your_long:
            content = all_content[reading_index:reading_index + your_long]
        else:
            content = all_content[reading_index:]
        first_simbol_on_next_str = content[-1]
        if first_simbol_on_next_str != " " and first_simbol_on_next_str != ".":
            last_space = content.rindex(' ')
            content = content[:last_space]
        else:
            content = content[:-1]

        reading_index += len(content) + 1
        content = content.strip()

        len_content = len(content)
        number_of_space = 0
        for i in content:
            if i == " ":
                number_of_space += 1
            else:
                continue

        while len_content < your_long:
            m = len_content
            difference = your_long - len_content
            content = content.replace(" ", "  ", difference)
            len_content = len(content)
        content = content.strip()

        recepient.write(content+'\n')

print("Congratulations new_text2.txt created in the current folder!!!!")
