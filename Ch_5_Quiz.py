# Jose Hernandez
# 11/13/2017

fruit_sale = [("clementines (5lb box)", 8), ("small basket", 24), 
	("large basket", 38),("sm. box grapefruit", 25), 
	("lg. box grapefruit", 40), ("30 count oranges", 18), 
	("sm. box oranges", 25), ("lg. box oranges", 35), 
	("box red apples", 23), ("box gold apples", 23), 
	("box gala apples", 23)]

for fruit in fruit_sale:
	print(fruit[0].title() + ": " + "$" + str(fruit[1]))

order = [fruit_sale[2], fruit_sale[7]]
length = len(order)

if length == 1:
	print("\nYour item:")
	for item in order:
		print("\t" + item[0].title() + ": " + "$" + str(item[1]))
	print("Total Price: " + "$" + str(order[1]))
elif length == 2:
	print("\nYour items:")
	for item in order:
		print("\t" + item[0].title() + ": " + "$" + str(item[1]))
	print("Total Price: " + "$" + str(order[0][1] + order[1][1]))
elif length == 3:
	print("\nYour items:")
	for item in order:
		print("\t" + item[0].title() + ": " + "$" + str(item[1]))
	print("Total Price: " + "$" + str(order[0][1] + order[1][1] + order[2][1]))

