from hypothesis import given
from hypothesis import strategies as st

import unittest

from bluezero import tools


class Uint16(unittest.TestCase):
    @given(st.integers(0, 65535))
    def test(self, x):
        self.assertEqual(
            tools.uint16_to_int(tools.int_to_uint16(x)),
            x)


if __name__ == '__main__':
    unittest.main()
