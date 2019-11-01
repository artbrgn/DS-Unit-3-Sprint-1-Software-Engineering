from random import randint, sample, uniform
from acme import Product
from random import randint

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0]+' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        product = Product(name=name, price=price,
                          weight=weight, flammability=flammability)
        products.append(product)
    return products


def inventory_report(products):
    names = []
    prices = []
    weights = []
    flammable = []

    for product in generate_products():
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammable.append(product.flammability)

    unique_prod = len(products)
    avgerage_price = sum(prices) / len(prices)
    average_weight = sum(weights) / len(weights)
    average_flam = sum(flammable) / len(flammable)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', unique_prod)
    print('Average price:', avgerage_price)
    print('Average weight:', average_weight)
    print('Average flammability:', average_flam)


if __name__ == '__main__':
    inventory_report(generate_products())
