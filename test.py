import os
import unittest
import tempfile
import server



class BaseTestCase(unittest.TestCase):
    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()


    def tearDown(self):
        pass

    def test_simple(self):
        res = self.app.get('/', follow_redirects=True)
        self.assertEqual(res.status_code, 200)

    if __name__ == '__main__':
        unittest.main()