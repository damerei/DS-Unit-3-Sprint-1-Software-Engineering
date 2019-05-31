{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Methods to create reports on products\n",
    "'''\n",
    "from random import choice, randint, uniform\n",
    "from acme import Product\n",
    "\n",
    "\n",
    "def generate_products(quantity=30):\n",
    "    '''\n",
    "    Creating a random gallimaufry of products\n",
    "    '''\n",
    "    products = []\n",
    "    adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']\n",
    "    noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']\n",
    "\n",
    "    \n",
    "    for _ in range(quantity):\n",
    "        name = (choice(adjective) + ' ' + choice(noun))\n",
    "        price = randint(5, 100)\n",
    "        weight = randint(5, 100)\n",
    "        flammability = uniform(0, 2.5)\n",
    "        products.append(Product(name=name, price=price,\n",
    "                                weight=weight, flammability=flammability))\n",
    "\n",
    "    return products\n",
    "\n",
    "\n",
    "def inventory_report(products):\n",
    "    '''\n",
    "    Method to generate report\n",
    "    '''\n",
    "    names = []\n",
    "    agg_price = 0\n",
    "    agg_weight = 0\n",
    "    agg_flammability = 0\n",
    "    product_count = len(products)\n",
    "\n",
    "  \n",
    "    for product in products:\n",
    "        unique_names.append(product.name)\n",
    "        agg_price += product.price\n",
    "        agg_weight += product.weight\n",
    "        agg_flammability += product.flammability\n",
    "\n",
    "    # print report to screen\n",
    "    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')\n",
    "    print('Unique product names:', len(set(names)))\n",
    "    print('Average price:', (total_price/product_count))\n",
    "    print('Average weight:', (total_weight/product_count))\n",
    "    print('Average flammability:', (total_flammability/product_count))\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    inventory_report(generate_products())"
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
