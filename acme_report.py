#!/usr/bin/env python

   '''
   Methods for generating and reporting on lists of products
   '''
from random import randint, sample, uniform, choice
from acme import Product


def generate_products(quantity=30):
    '''
    Method for generating a gallimaufry of Acme products
    '''
    products = []
    adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    
    # create products with random values and append to products
    for _ in range(quantity):
        name = (choice(adjective) + ' ' + choice(noun))
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name=name, price=price,
                                weight=weight, flammability=flammability))
    
    return products

def inventory_report(products):
    '''
    Method for giving a report on the inventory
    '''
    names = []
    agg_price = 0
    agg_weight = 0
    agg_flammability = 0
    product_count = len(products)
    
    # gather information for report
    for product in products:
        unique_names.append(product.name)
        agg_price += product.price
        agg_weight += product.weight
        agg_flammability += product.flammability
    
    # print report to screen
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', len(set(names)))
    print('Average price:', (agg_price/product_count))
    print('Average weight:', (agg_weight/product_count))
    print('Average flammability:', (agg_flammability/product_count))


if __name__ == '__main__':
    inventory_report(generate_products())
