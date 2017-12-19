'''Classes used to represent users and an admin, along with the admin's
	privileges.'''

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
	
	def incrementLoginAttempts(self):
		'''Increment the amount of attempts by 1.'''
		self.loginAttempts += 1
	
	def resetLoginAttempts(self):
		'''Reset the amount of attempts to 0.'''
		self.loginAttempts = 0


class Privileges():
	'''Privileges of an admin.'''
	
	def __init__(self):
		'''Privilege attributes.'''
		self.privileges = ["can add post", "can delete post", "can ban user"]
	
	def showPrivileges(self):
		'''Print the list of privileges the admin has.'''
		print("ADMIN PRIVILEGES")
		print("------------------")
		for p in self.privileges:
			print("-" + p.upper())


class Admin(User):
	'''Specific admin profile.'''
	
	def __init__(self, firstName, lastName, age, gender):
		'''Initialize admin profile with parent class.'''
		super().__init__(firstName, lastName, age, gender)
		self.privileges = Privileges()

