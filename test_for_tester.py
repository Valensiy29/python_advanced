import unittest

from python_advanced_2.python_advanced import ages

class Test(unittest.TestCase):
    def test_correct_age(self):
        age = 12
        ex_age = 'teenager'
        func_res = ages(age)
        self.assertEqual(ex_age,func_res)