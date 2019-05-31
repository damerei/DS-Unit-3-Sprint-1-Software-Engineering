#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, inventory_report
from acme_report import ADJECTIVES, NOUN



class AcmeProductTests(unittest.TestCase):
    '''
    Making sure Acme products are the tops!
    '''
    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
        

class AcmeReportTests(unittest.TestCase):
    '''
    Making sure Acme products are the tops!
    '''
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

        for product in products:
            prod_name = product.name.split()
            adjective = prod_name[0]
            noun = prod_name[1]
            self.assertIn(adjective, adjectives)
            self.assertIn(noun, nouns)



if __name__ == '__main__':
    unittest.main()
