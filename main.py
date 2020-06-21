from functools import lru_cache

@lru_cache(maxsize=100)
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)


@lru_cache(maxsize=100)
def factorial(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return n * factorial(n-1)


@lru_cache(maxsize=100)
def my_sequence(n):
	
	len_of_n = len(str(n))
	if n < 12:
		return n
	elif len_of_n % 14 > 9 or len_of_n % 123 == 13:
		return my_sequence(n-1 + 13)
	else:
		return my_sequence(n-1) + my_sequence(n-2) + my_sequence(2)



class Person():
	def __init__(self, name, age, height, pets_names):
		self.name = name
		self.age = age
		self.height = height
		self.pets_names = pets_names
	
	def add_pet_name(self, pet_name):
		self.pets_names.append(pet_name)

	def remove_pet_name(self, pet_name): # :'(
		self.pets_names.remove(pet_name)
