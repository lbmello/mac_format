
import unittest

from mac_format.mac_formater import MacFormater


class MyTest(unittest.TestCase):
    example_mac = 'b0:4f:13:d1:14:41'
    mac_address = MacFormater(example_mac)

    def test_mac_formater(self):
        self.assertIn(MyTest.example_mac, MyTest.mac_address.return_exit())


    def test_vendor_return(self):
        self.assertIsNotNone(MyTest.mac_address.mac_vendor())