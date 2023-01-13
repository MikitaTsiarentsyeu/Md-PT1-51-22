class FreightTrain:

    def __init__(self, cart_count) -> None:
        self.cart_count = cart_count

    def __str__(self) -> str:
        return f"I'm a train of {self.cart_count} carts, choo-choo!"

    def __int__(self):
        return self.cart_count

    def __add__(self, other):
        # if isinstance(self, FreightTrain) and isinstance(other, FreightTrain):
        try:
            return FreightTrain(self.cart_count+other.cart_count)
        except:
            raise TypeError("cannot add non-FreightTrain objects")

    def __eq__(self, other):
        if self.cart_count == other.cart_count:
            return True
        else:
            return False

shorty = FreightTrain(3)
looong = FreightTrain(20)
print(shorty)

print(int(shorty))

print(shorty + looong)

print(looong == shorty)