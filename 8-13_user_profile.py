# Jose Hernandez
# 11/17/2017

def buildProfile(first, last, **userInfo):
	profile = {}
	profile["first name"] = first
	profile["last name"] = last
	for key, value in userInfo.items():
		profile[key] = str(value)
	return profile

jose = buildProfile("jose", "hernandez", location = "fort wayne", age = 17,
		gender = "male")

print(jose)
