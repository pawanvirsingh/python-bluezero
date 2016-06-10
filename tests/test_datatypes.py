import unittest

from bluezero import tools


class Uint16(unittest.TestCase):
    def test_roundtrip(self):
        test_values = [0, 12, 256, 33333, 65535]
        for x in test_values:
            self.assertEqual(
                tools.uint16_to_int(tools.int_to_uint16(x)),
                x)

    def test_exception(self):
        test_values = [-70000, -65535, -1, 65536, 70000]
        with self.assertRaises(ValueError):
            for x in test_values:
                tools.int_to_uint16(x)

if __name__ == '__main__':
    unittest.main()
