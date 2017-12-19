# Jose Hernandez
# 12/1/2017

import json

def getStoredUsername():
	'''Get stored username if available.'''
	fileName = "username.json"
	try:
		with open(fileName) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username


def getNewUsername():
	'''Prompt for a new username.'''
	username = input("What is your name? ")
	fileName = "username.json"
	with open(fileName, "w") as f_obj:
		json.dump(username, f_obj)
	return username


def greetUser():
	'''Greet the user by name.'''
	username = getStoredUsername()
	if username:
		check_username = input("Is " + username + ", the correct username?" + 
			" ('yes' or 'no') ")
		if check_username == "yes":
			print("Welcome back, " + username + "!")
		elif check_username == "no":
			getNewUsername()
		else:
			print("You did not verify if the username was correct. This program"
				+ " will now close.")
	else:
		username = getNewUsername()
		print("We'll remember you when you come back, " + username + "!")


greetUser()
