#this code serves as a coffee vending machine which gives back the change

products = ['espresso', 'double espresso', 'capuccino', 'macchiato']
price_products = [1.20, 2.00, 1.80, 2.20]

print(products)
print(price_products)

request = input("What drink do you want ?")
index = products.index(request) 
#should it be str
price = price_products[index]

money_inserted = input("How much money is inserted in the machine ?")
int_money = int(money_inserted)
change = int_money - price

if change < 0:
	print('Not enough money !')

change_2 = change_1 = change_050 = change_020 = change_010 = 0

while change > 0:
	if change >= 2:
		change = change - 2
		change_2 = change_2 + 1
	elif change >= 1:
		change = change - 1
		change_1 = change_1 + 1
	elif change >= 0.50:
		change = change - 0.50
		change_050 = change_050 + 1
	elif change >= 0.20:
		change = change - 0.20
		change_020 = change_020 + 1
	elif change >= 0.10:
		change = change - 0.10
		change_010 = change_010 + 1
	else:
		change = 0

print("Number of 2€ coins is: " + str(change_2))
print("Number of 1€ coins is: " + str(change_1))
print("Number of 50c coins is: " + str(change_050))
print("Number of 20c coins is: " + str(change_020))
print("Number of 10c coins is: " + str(change_010))