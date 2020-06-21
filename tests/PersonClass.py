import main
import unittest

class Test_Person_Class(unittest.TestCase):
	def test_user_creation(self):
		test_user = main.Person("Jonathan Newgent", 12, "5' 12\"", ['Goldy Fishy', 'Birdy'])
		self.assertEqual(test_user.name, "Jonathan Newgent")
		self.assertEqual(test_user.height, "5' 12\"")
		self.assertEqual(test_user.age, 12)
		self.assertEqual(test_user.pets_names, ['Goldy Fishy', 'Birdy'])

	def test_pet_addition(self):
		test_user = main.Person("Jonathan Newgent", 12, "5' 12\"", ['Goldy Fishy', 'Birdy'])
		test_user.add_pet_name('Cookie')
		self.assertEqual(test_user.pets_names, ['Goldy Fishy', 'Birdy', 'Cookie'])
		test_user.add_pet_name('Samantha')
		self.assertEqual(test_user.pets_names, ['Goldy Fishy', 'Birdy', 'Cookie', 'Samantha'])

	def test_pet_deletion(self):
		test_user = main.Person("Jonathan Newgent", 12, "5' 12\"", ['Goldy Fishy', 'Birdy'])
		test_user.remove_pet_name('Goldy Fishy')
		self.assertEqual(test_user.pets_names, ['Birdy'])
		test_user.remove_pet_name('Birdy')
		self.assertEqual(test_user.pets_names, [])




if __name__ == '__main__':
	unittest.main()