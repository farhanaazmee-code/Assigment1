customer_name = input("Enter customer's name: ")

product1 = input("Enter product name: ")
price1 = float(input("Enter the price: "))

product2 = input("Enter product name: ")
price2 = float(input("Enter the price: "))

product3 = input("Enter product name: ")
price3 = float(input("Enter the price: "))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.0

discount = subtotal * discount_rate
final_total = subtotal - discount

print(f"\nCustomer Name: {customer_name}")
print(f"Product Name: {product1}")
print(f"Price: {price1}")
print(f"Product Name: {product2}")
print(f"Price: {price2}")
print(f"Product Name: {product3}")
print(f"Price: {price3}")
print(f"Subtotal is: {subtotal}")
print(f"Discount is: {discount}")
print(f"Final Total is: {final_total}")

