import unittest
from random import choices

from pyping_py3 import ping, UnknownHostError, Response

class PingTest(unittest.TestCase):


    def setUp(self):
        pass

    def test_ping_known_host(self):
        assert isinstance(ping(hostname='localhost'), Response)

    def test_ping_unknown_host(self):
        exc = None
        try:
            ping(hostname=''.join(choices('qwertyuiopasdfghjklzxcvbnm', k=15)))
        except Exception as e:
            exc = e

        self.assertIsInstance(exc, UnknownHostError,'no exception on ping unknown host')



if __name__ == '__main__':
    unittest.main()
