import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability(self):
        product_low = Product('low', price=1, weight=4, flammability=1)
        self.assertEqual(product_low.stealability(), "Not so stealable...")

        product_medium = Product('medium', price=2, weight=4, flammability=4)
        self.assertEqual(product_medium.stealability(), "Kinda stealable.")

        product_high = Product('high', price=4, weight=4, flammability=15)
        self.assertEqual(product_high.stealability(), "Very stealable!")

    def test_explode(self):
        product_low = Product('low', price=1, weight=4, flammability=1)
        self.assertEqual(product_low.explode(), "...fizzle.")

        product_medium = Product('medium', price=2, weight=4, flammability=4)
        self.assertEqual(product_medium.explode(), "...boom!")

        product_high = Product('high', price=4, weight=4, flammability=15)
        self.assertEqual(product_high.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        product_list = generate_products()
        self.assertEqual(len(product_list), 30)

    def test_legal_names(self):
        product_list = generate_products()
        for product in product_list:
            words = product.name.split(sep=' ')
            self.assertEqual(len(words), 2)
            self.assertIn(words[0], ADJECTIVES)
            self.assertIn(words[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
