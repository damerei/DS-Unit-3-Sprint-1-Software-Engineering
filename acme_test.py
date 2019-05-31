{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python\n",
    "\n",
    "import unittest\n",
    "from acme import Product\n",
    "from acme_report import generate_products\n",
    "\n",
    "class AcmeProductTests(unittest.TestCase):\n",
    "    '''\n",
    "    Making sure Acme products are the tops!\n",
    "    '''\n",
    "    def test_default_product_price(self):\n",
    "        prod = Product('Test Product')\n",
    "        self.assertEqual(prod.price, 10)\n",
    "\n",
    "    def test_default_product_weight(self):\n",
    "        prod = Product('Test Product')\n",
    "        self.assertEqual(prod.weight, 20)\n",
    "\n",
    "    def test_stealable_explodey(self):\n",
    "        prod = Product('Dynamite', 1000, 1, 100)\n",
    "        self.assertEqual(prod.explode(), '...BABOOM!!')\n",
    "        self.assertEqual(prod.stealability(), 'Very stealable!')\n",
    "        \n",
    "        \n",
    "class AcmeReportTests(unittest.TestCase):\n",
    "    '''\n",
    "    make sure Acme Reports are the tops!\n",
    "    '''\n",
    "    def test_default_num_products(self):\n",
    "        products = generate_products()\n",
    "        self.assertEqual(len(products), 30)\n",
    "\n",
    "    def test_legal_names(self):\n",
    "        products = generate_products()\n",
    "        adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']\n",
    "        nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']\n",
    "\n",
    "        for product in products:\n",
    "            prod_name = product.name.split()\n",
    "            adjective = prod_name[0]\n",
    "            noun = prod_name[1]\n",
    "            self.assertIn(adjective, adjectives)\n",
    "            self.assertIn(noun, nouns)\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
