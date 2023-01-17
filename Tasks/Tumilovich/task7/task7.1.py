def reverse(text):
    if len(text) == 1:
        return text
    else:
        return text[-1] + reverse(text[:-1])

print(reverse('PYTHON-RULEZ!'))
