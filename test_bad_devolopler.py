import datetime
import unittest

from python_advanced_2.python_advanced import Person

class Tester(unittest.TestCase):
    def test_get_age(self):
        Person(address='work 24/23',name='valentine',year_of_birth = 2009)
        year_of_birth = 2009
        func = Person.get_age(self)
        res = year_of_birth - datetime.datetime.now().year
        self.assertEqual(res,func)
