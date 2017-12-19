# Jose Hernandez
# 11/14/2017

sandwich_orders = ["tuna sandwich", "pastrami sandwich", "club sandwich",
	"hamburger", "ham and cheese sandwich"]
	
finished_sandwiches = []

print("The deli has run out of pastrami.")
while "pastrami sandwich" in sandwich_orders:
	sandwich_orders.remove("pastrami sandwich")

for sandwich in sandwich_orders:
	print("\nYour " + sandwich + " has been made.")

while sandwich_orders:
	fin_sandwich = sandwich_orders.pop()
	finished_sandwiches.append(fin_sandwich)
	
print("\n---- Sandwiches Made ----")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())

