import unittest
import math

def errorDefMax(a,b):
    if a != b:
        raise ValueError ("The radius caanot be negative")
    return max(a,b)


class TestMaxMinMath(unittest.TestCase):

	def test_correct_param_max(self):
		expected = 5
		test_data = [1,2,3,4,5]
		my_max = max(test_data)
		self.assertEqual(max(test_data), expected)
		#print('The Max Number Is:', my_max)

	def test_correct_param_min(self):
		expected = 1
		test_data = [1,2,3,4,5]
		self.assertEqual(min(test_data), expected)

	#def test_wrong_param_max(self):
		#with self.assertRaises(ValueError):
			#self.assertEqual(max(), True)


if __name__ == '__main__':
    unittest.main()
