"""
⭐⭐⭐ Exercise 4 – Shopping Cart

1. Product (use @dataclass): name (str), price (float)
2. ShoppingCart:
     - add(product, quantity=1)   → adds (or increases quantity of) a product
     - remove(product_name)       → removes it completely; raise KeyError if missing
     - total()                    → sum of price * quantity
     - apply_discount(percent)    → future total() calls are reduced by that %
     - __len__                    → total number of ITEMS (sum of quantities)
     - __str__                    → a receipt, one line per product, then the total

Hint: store items in a dict  {product_name: [product, quantity]}
"""
from dataclasses import dataclass

# Write your code here 👇


cart = ShoppingCart()
bread = Product("Bread", 2.50)
milk = Product("Milk", 1.20)
cart.add(bread, 2)
cart.add(milk)
cart.add(milk)
assert len(cart) == 4
assert cart.total() == 7.40
cart.apply_discount(10)
assert round(cart.total(), 2) == 6.66
cart.remove("Bread")
assert len(cart) == 2
print(cart)
print("✅ All checks passed!")
