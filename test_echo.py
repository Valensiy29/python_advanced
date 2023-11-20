import unittest

from python_advanced_2.python_advanced import app2,have_a_nice_day

class Tester(unittest.TestCase):
    def setUp(self) -> None:
        app2.config['TESTING'] = True
        app2.config['DEBUG'] = False
        self.app2 = app2.test_client()
        self.base_url = '/hello/'
    def test_can_get_correct_username_with_weekdate(self):

        username_1 = 'Привет valentine! Хорошего понедельника'
        username = 'valentine'
        func_2 = have_a_nice_day(username)

        self.assertEqual(username_1,func_2)

    def tearDown(self) -> None:
        pass
