class Dog:
	def __init__(self):
		self.name = "Dog"
		print("Dog was Born")
	def speak(self):
		print("YELP, YELP!", self.name)

	def test(self):
		print("Dog's test")

	def __del__(self):
		print("destroy!!")


class Puppy(Dog):
	def __init__(self):
		self.name = "Puppy"
		self._age = 7
		print("Puppy was Born")
        
	def __init__(self, name):
		self.name = name
		print(name, "was Born")

	def get_age(self):
		return self._age

	def test(self):
		print("Puppy's test")
		self.__q()

	def __q(self):
		print("qqqqqqqqqqqq")

	


puppy = Puppy('PP')
puppy.speak()
# print(puppy.name, puppy.get_age(), isinstance(puppy, Dog))
puppy.test()
puppy.__q()
