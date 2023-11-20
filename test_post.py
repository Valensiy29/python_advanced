import unittest
from post_request1 import array_sum,post

class test(unittest.TestCase):
    def setup(self):
        post.config['TESTING'] = True
        post.config['DEBUG'] = False
        self.post = post.test_client()
        self.base_url = '/cor_check'
    def test(self):
        func = array_sum
        