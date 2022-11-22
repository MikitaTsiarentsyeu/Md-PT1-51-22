lim = int(input("Please enter a number of characters per line in the range greater than 35: \n"))


def get_number_letters(l):
    cnt = 0
    for w in l:
        cnt += len(w)
    return cnt


def get_line_with_limit_length(words):
    cnt = get_number_letters(words)

    n = lim - cnt
    result = ""
    n_worlds = len(words) - 1

    for word in words:
        if n_worlds == 0:
            result += word
            break

        t = n // n_worlds
        p = n % n_worlds

        x = t + 1 if p > 0 else t

        result += word + " " * x
        n -= x
        n_worlds -= 1

    return result


def wrap_text(text, size):
    result = []
    for line in text:
        if line == "":
            result.append("")

        w = 0
        bank = []
        for word in line.split():
            if w + len(word) + 1 <= size:
                bank.append(word)
                w += len(word) + 1
            else:
                result.append(get_line_with_limit_length(bank))
                bank = [word]
                w = len(word) + 1

        if len(bank):
            result.append(" ".join(bank))

    return "\n".join(result)


with open('text.txt', 'r', encoding='utf-8') as file:

    name = f'Kavalchuk_{lim}_symbols.txt'

    with open(name, 'a', encoding='utf-8') as my_file:
        text = [line.strip() for line in file]

        my_file.write(wrap_text(text, lim))

        print(f"You created a file {name} with line length {lim} characters")

