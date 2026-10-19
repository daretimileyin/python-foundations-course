price = float(input("Item price: "))
quantity = int(input("Quantity: "))
tax_rate = float(input("Tax rate (%): "))
tip_rate = float(input("Tip (%): "))

subtotal = price * quantity
tax = subtotal * tax_rate / 100
tip = subtotal * tip_rate / 100
total = subtotal + tax + tip

print(f"Subtotal:   ${subtotal:.2f}")
print(f"Tax ({tax_rate}%): ${tax:.2f}")
print(f"Tip ({tip_rate}%):  ${tip:.2f}")
print("-" * 18)
print(f"TOTAL:      ${total:.2f}")
