'''
Initial set of classes for Acme products
'''

from random import randint


class Product:
    '''
    Class to create acme products. 
    '''
    def __init__(self, name, price=10, weight=20,
                 flammability=.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        '''
        calculating stealability as a function of price to weight
        '''
        steal_ratio = self.price / self.weight
        if steal_ratio < .5:
            return 'Not so stealable...'
        elif steal_ratio < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        '''
        calculate volatility, estimate likelihood of explosion
        '''
        volatility = self.flammability * self.weight
        if volatility < 10:
            return '...fizzle'
        elif volatility < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

        
class BoxingGlove(Product):
    '''
    Acme Booxing Glove is an instantiation of the class Product
    
    '''
    def __init__(self, name, price=10, weight=10,
                 flammability=.5, identifier=randint(1000000, 9999999)):
    
            super().__init__(name=name, price=price, weight=weight,
                     flammability=flammability,
                     identifier=identifier)
    def explode(self):
        '''
        overwrite explode function to remind you gloves usually aren't volatile
        '''
        return "...it's a glove."

    def punch(self):
        '''
        translate the glove weight into an assessment of how much it
        will hurt to be hit by
        Output:
        return phrase assess punch hurtiness
        '''
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
