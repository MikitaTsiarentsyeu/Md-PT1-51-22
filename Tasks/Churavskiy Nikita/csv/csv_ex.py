import csv, json, pickle

new_dict = {
        'Model': ['80 1.6 Specs', '80 1.6 Specs', '80 1.8 Specs','80 1.8 Specs',
                '80 1.8 S Specs','80 1.9 E Specs', '80 1.9 E Quattro Specs'],
        'Year': ['1989', '1993', '1986','1989','1986','1986', '1986'],
        'Horsepower': ['69', '102', '75','90','88','113', '113'],
        'Engine size': ['1595 cm3 (97.3 cu-in)', '1595 cm3 (97.3 cu-in)', '1781 cm3 (108.7 cu-in)','1781 cm3 (108.7 cu-in)',
                        '1781 cm3 (108.7 cu-in)','1847 cm3 (112.7 cu-in)', '1847 cm3 (112.7 cu-in)']
}

new_dict1 = str(new_dict).replace("'","#").replace('#','"')

def new_type_files():
    with open('new_file.csv', 'r+') as r:
        values_app = ''.join([i+',' for i in new_dict])
        r.write(values_app[0:len(values_app)-1]+'\n')
        for i in range(len(new_dict['Model'])):
            r.write(new_dict['Model'][i]+',')
            r.write(new_dict['Year'][i]+',')
            r.write(new_dict['Horsepower'][i]+',')
            r.write(new_dict['Engine size'][i]+'\n')

    with open('file_new.json', 'w+') as f:
        json.dump(new_dict1,f)

    with open('file_new2.pickle', 'wb+') as h:
        pickle.dump(new_dict1,h)

    return f'fail in format csv: new_file.csv\nfail in format json: file_new.csv\nfail in format pickle: file_new2.pickle'

print(new_type_files())
