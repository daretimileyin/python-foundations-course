from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


class ShoppingCart:
    def __init__(self):
        self.items = {}          # name -> [product, quantity]
        self.discount = 0

    def add(self, product, quantity=1):
        if product.name in self.items:
            self.items[product.name][1] += quantity
        else:
            self.items[product.name] = [product, quantity]

    def remove(self, product_name):
        if product_name not in self.items:
            raise KeyError(f"{product_name} is not in the cart")
        del self.items[product_name]

    def subtotal(self):
        return sum(p.price * q for p, q in self.items.values())

    def total(self):
        return round(self.subtotal() * (1 - self.discount / 100), 2)

    def apply_discount(self, percent):
        self.discount = percent

    def __len__(self):
        return sum(q for _, q in self.items.values())

    def __str__(self):
        lines = [f"{q} x {p.name:<10} {p.price * q:>7.2f}" for p, q in self.items.values()]
        if self.discount:
            lines.append(f"Discount: {self.discount}%")
        lines.append(f"TOTAL: {self.total():.2f}")
        return "\n".join(lines)


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
