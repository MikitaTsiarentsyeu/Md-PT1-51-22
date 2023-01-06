import os, const, validation


def read_text():
    if validation.valid_3(const.directory_csv) == True: 
        with open(const.directory_csv, 'r+') as f:
            return f.read()
    else:
        raise RuntimeError('Not correctly path')


def write_text(fin_res):
    if validation.valid_3(const.directory_write) == True: 
        with open(const.directory_write, 'a+') as f:
            f.write(fin_res)
    else:
        raise RuntimeError('Not correctly path')
    