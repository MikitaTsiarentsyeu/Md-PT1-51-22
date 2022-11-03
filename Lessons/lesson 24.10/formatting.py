
"a cat, a dog and a parrot"
c, d, p = "cat", "dog", "parrot"

r = "a " + c + ", a " + d + " and a " + p 
print(r)

"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a "
"a cat, a dog and a parrot"

print("a {}, a {} and a {}".format(c, d, p))
print("a {}, a {} and a {}".format(p, c, d))
print("a {}, a {} and a {}".format(c, c, c))
# print("a {}, a {} and a {}".format(c, d)) error

print("a {1}, a {2} and a {0}".format(c, d, p))
print("a {c_name}, a {d_name} and a {p_name}".format(c_name=c, d_name=d, p_name=p))

cat_count = 1
print(f"a {'3 '+c+'s' if cat_count > 1 else 'cat'}, a {d+d} and a {p.capitalize()}")

print("%s %d" % ("old style formatting mode enabled:", 666)) # old style, please do not use,for god sake

