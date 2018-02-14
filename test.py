from server import app
# import os
import unittest
# import tempfile



class BaseTestCase(unittest.TestCase):
    # def setUp(self):
    #     # server.app.config['TESTING'] = True
    #     # self.app = server.app.test_client()
    #     pass


    # def tearDown(self):
    #     pass

    def test_index(self):
        # app.config['TESTING'] = True
        tester = app.test_client(self)
        res = tester.get('/')
        self.assertEqual(res.status_code, 200)
        # res = self.app.get('/', follow_redirects=True)
        # self.assertEqual(res.status_code, 200)
        # self.assertTrue(True)

    if __name__ == '__main__':
        unittest.main()

BaseTestCase()