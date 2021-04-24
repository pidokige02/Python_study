def add(a, b): return a + b

print("9999999999999999999999999999999999999 Dog in br1")
	
class Dog:
	def __init__(self, name):
		self.name = name
		self.color = "Blue"
		print(self.name, "was Born")
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

	def speak(self):
		print("YELP!", self.name)

	def __del__(self):
			print("destroy!!")

class Puppy(Dog):
	name = "강아지"

	def __init__(self):
		self.name = "Puppy"
		self.color = "Red"
		print("QQQQ> Puppy was Born", self.name)
	
	def __read_diary(self):
		print("Diary content!!!!!")

	def speak(self):
		self.age = 234
		print("Bow wow!", self.name)

	def wag(self):
		self.__read_diary()
		print("Puppy's wag tail")

	def tto():
		print("Ttooooooooooo0000000000")

class Calc:
	def plus(a, b):
		return a + b

d = Dog('puddle')
p = Puppy()
d.speak()
p.speak()
# d.wag()
p.wag()

Puppy.tto()
# p.tto()

print("cal=", Calc.plus(1, 2))

# p.__read_diary()

print("aaaaa", d.name, p.name, Puppy.name)

print("QQQ>>", isinstance(p, Dog), p == None)