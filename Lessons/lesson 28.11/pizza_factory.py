def prepare():
    print("STGARTING A NEW PIZZA")
    print("preparing a base")
    print("adding a sauce")

def add_ingridient(ingridient):
    print(f"adding {ingridient}")

def grind_cheese():
    print("griding cheese")

def bake(t):
    print(f"baking at {t} degrees")

def done():
    print("slicing")
    print("boxing")
    print("DONE!")


# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(200)
#     done()

# def make_double_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(200)
#     done()

# def make_4_cheeses():
#     prepare()
#     add_ingridient("chedder")
#     add_ingridient("mozzarela")
#     add_ingridient("cordon-blue")
#     add_ingridient("parmejano")
#     bake(150)
#     done()

def pizza_factory(ingridients, t, need_grind_cheese=True):
    def factory_method():
        prepare()
        for i in ingridients:
            add_ingridient(i)
        if need_grind_cheese:
            grind_cheese()
        bake(t)
        done()
    return factory_method

make_pepperoni = pizza_factory(["pepperoni"], 200)
make_double_pepperoni = pizza_factory(["pepperoni", "pepperoni"], 200)
make_4_cheeses = pizza_factory(["chedder", "mozzarela", "cordon-blue", "parmejano"], 200, False)

make_pepperoni()