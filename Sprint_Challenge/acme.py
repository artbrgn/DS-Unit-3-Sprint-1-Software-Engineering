from random import randint


class Product:
    '''Model for Products
    '''

    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        steal = self.price/self.weight
        if steal < 0.5:
            return "Not so stealable..."
        elif steal < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        boom = self.flammability*self.weight
        if boom < 10:
            return "...fizzle."
        elif boom < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    '''Override certain parameters of the default class and add some
    functionality unique to BoxingGlove
    '''

    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=10,
                         flammability=flammability, identifier=identifier)

    def explode(self):
        boom = "...it's a glove."
        return boom

    def punch(self):
        weight = self.weight
        if weight < 5:
            return "That tickles."
        elif weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
