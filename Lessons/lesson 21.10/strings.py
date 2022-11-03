x = "test"
y = 'test'
print(type(x), type(y), x==y)

print('my dog\'s name is "Zephyrka"')

line = "my\tfirst\tline\nmy\tsecond\tline"
print(line)

line = '''my   first   line
my  second  line'''
print(line)

s = "my very long string"
print(len(s))
print(s[0], s[1], s[2], s[3], s[4])
print(s[len(s)-1])
print(s[18])
print(s[-1], s[-2], s[-3])
print(s[-19])

print(s[0:3])
print(s[0:7])
print(s[8:12])
print(s[8], s[9], s[10], s[11])

print(s[3:-3])
print(s[:])
print(s[3:])
print(s[:12])

print(s[::3])
print(s[::-1])

x = "TeSt_StRiNg"

print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.casefold())
print(x)

print(x.upper().lower().capitalize())

print(repr(str(5)))
print(repr(5))
print(repr("  test     ".strip()))

print(repr("    test     ".replace(" ", "")))

print(repr("  my senseless str     ".strip()))
print(repr("    my senseless str     ".replace(" ", "")))

print("553-6786-43564".replace('-', "DASH").replace("DASH", ':'))

s = "test str with some symbols in it"

print(' ' in s)
print('!' in s)
print("str" in s)
print('string' in s)

print(s.find(' '))
print(s.find('test'))
print(s.find('str'))
print(s.find('  '))

print("str1"+"str2"+"str3"+"str4"+"str5")
"str1str2"
"str1str2str3"
"str1str2str3str4"
"str1str2str3str4str5"

print("mult"*555)

print(s.split())
print(type(s.split()))
print(s.split('s'))
print('_'.join(s.split()))

code = "f6fu6r6:adidas-sprstr33"
print(code.split(':')[1].split('-'))