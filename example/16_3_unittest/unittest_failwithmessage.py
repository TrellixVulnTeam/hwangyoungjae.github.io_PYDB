# unittest_failwithmessage.py
import unittest


class FailureMessageTest(unittest.TestCase):
    def testFail(self):
        self.assertFalse(True, 'failure message goes hre')

