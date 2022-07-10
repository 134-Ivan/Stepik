


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

tv_1 = TV('samsung', 1000)
tv_2 = TV('LG', 2000)
tbl = Table('Ikea', 500)
nb_1 = Notebook('asus', 3000)
nb_2 = Notebook('lenovo', 900)
cp = Cup('twix', 10)

cart = Cart()
cart.add(tv_1)
cart.add(tv_2)
cart.add(tbl)
cart.add(nb_1)
cart.add(nb_2)
cart.add(cp)

print(cart.get_list())
