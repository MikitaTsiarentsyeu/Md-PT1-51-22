def maker(n):
    def action(x):
        return x**n
    return action

square = maker(2)

print(type(square))
print(square(10))


cube = maker(3)
print(cube(10))

powers = []
for i in range(6):
    powers.append(maker(i))

print(powers)
for power in powers:
    print(power(10))

print(maker(10)(2))