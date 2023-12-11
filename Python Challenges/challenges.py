import random

def dis(price, discount):
	discount = (discount / 100) * price
	return price - discount


test_number = [100, 75, 50, 25, 20, 10, 5]
random_price = random.choice(test_number)
random_discount = random.choice(test_number)
print(f"The price is: $ {random_price}")
print(f"The discount should be: {random_discount}%")
print(dis(price = random_price,discount = random_discount))