# Jose Hernandez
# 11/29/2017
# Counts the number of times a word comes up.

odyssey = "the_odyssey.txt"
iliad = "the_iliad.txt"

print("The Odyssey, 'the' word count:")
with open(odyssey, encoding="utf-8") as file_object:
	contents = file_object.read()
	number_of_the = contents.lower().count("the")
	print(number_of_the)

print("")

print("The Iliad, 'the' word count:")
with open(iliad, encoding="utf-8") as file_object:
	contents = file_object.read()
	number_of_the = contents.lower().count("the")
	print(number_of_the)

