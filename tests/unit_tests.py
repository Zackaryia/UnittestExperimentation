import main
import unittest

class Test_Algorithems_Sequences(unittest.TestCase):
	def test_fibonacci(self):
		self.assertEqual(main.fibonacci(91), 4660046610375530309)
		self.assertEqual(main.fibonacci(31), 1346269)
		self.assertEqual(main.fibonacci(0), 0)
		self.assertEqual(main.fibonacci(1), 1)
		self.assertEqual(main.fibonacci(199), 173402521172797813159685037284371942044301)
		self.assertEqual(main.fibonacci(310), 27332759203762391000908267962175339332906872716290689783750745455)

	def test_my_sequence(self):
		self.assertEqual(main.my_sequence(0), 0)
		self.assertEqual(main.my_sequence(10), 10)
		self.assertEqual(main.my_sequence(95), 5302049185640998659)
		self.assertEqual(main.my_sequence(51), 3380551691)

	def test_factorial(self):
		self.assertEqual(main.factorial(0), 0)
		self.assertEqual(main.factorial(13), 6227020800)
		self.assertEqual(main.factorial(27), 10888869450418352160768000000)
		self.assertEqual(main.factorial(9), 362880)

	def test_compound_algorithem(self):
		self.assertEqual(main.my_sequence(main.factorial(4)), 7695) # 24th my sequence number
		self.assertEqual(main.fibonacci(main.factorial(5)), 5358359254990966640871840) # the 120th fibinaci number
		self.assertEqual(main.fibonacci(main.my_sequence(16)), 3210056809456107725247980776292056) # 162th fibinaci number


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