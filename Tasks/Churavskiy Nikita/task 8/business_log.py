import os, string, const
import reader_writer


def fnc_1(name):
    text = reader_writer.read_text().replace("\n",",").split(',')
    value = const.Countries[name]
    return f"{', '.join(text[0:4])}\n{', '.join((text[text.index(value):text.index(value)+4]))}"


def lst_dct():
    some = ''.join([str(i[0]) + ':' + str(i[1]) + '\n' for i in list(map(list,const.Countries.items()))])
    some = some.strip().replace('Italy,', 'Italy')
    return some


def res_lst1(country):
    lst_1 = [i for i in country if i in string.punctuation]
    lst_2 = [i for i in country if i in string.digits]
    return lst_1+lst_2

    
def res_lst2(population):
    lst_1 = [i for i in population if i in string.punctuation.replace('.','')]
    lst_2 = [i for i in population if i.lower() in string.ascii_lowercase]
    return lst_1+lst_2


def res_lst3(currency):
    lst_1 =  lst_1 = [i for i in currency if i in string.punctuation]
    lst_2 = [i for i in currency if i in string.ascii_lowercase]
    return lst_1+lst_2


def res_csv(name1,name2,name3,name4):
    fin_res = str(name1+','+name2+','+name3+','+name4+'\n')
    if isinstance(fin_res,str):
        write_csv(fin_res)
    else:
        raise RuntimeError("Fail not write, not correctly parametr")
     

def write_csv(fin_res):
    reader_writer.write_text(fin_res)
   
   




