# Jose Hernandez
# 11/20/2017

class User():
	'''A user profile.'''
	
	def __init__(self, firstName, lastName, age, gender):
		'''Initialize attributes of a user.'''
		self.firstName = firstName
		self.lastName = lastName
		self.age = str(age)
		self.gender = gender
		self.loginAttempts = 0
	
	def describeUser(self):
		'''Summary of the user's information.'''
		print("First Name: " + self.firstName.title())
		print("Last Name: " + self.lastName.title())
		print("Age: " + self.age)
		print("Gender: " + self.gender.title())
	
	def greetUser(self):
		'''Personalized greeting to the user.'''
		print("Hello " + self.firstName.title() + " " + self.lastName.title() +
		".")
	
	def incrementLoginAttempts(self, inc=1):
		'''Increment the amount of attempts by inc.'''
		self.loginAttempts += inc
	
	def resetLoginAttempts(self):
		'''Reset the amount of attempts to 0.'''
		self.loginAttempts = 0

firstUser = User("jose", "hernandez", 17, "male")
firstUser.incrementLoginAttempts(2)
print("Login attempts: " + str(firstUser.loginAttempts))

firstUser.incrementLoginAttempts(5)
print("\nLogin attempts: " + str(firstUser.loginAttempts))

firstUser.incrementLoginAttempts(10)
print("\nLogin attempts: " + str(firstUser.loginAttempts))

firstUser.resetLoginAttempts()
print("\nLogin attempts: " + str(firstUser.loginAttempts))
