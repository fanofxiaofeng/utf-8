#!/usr/local/bin/python3

import impl
import unittest


class Test(unittest.TestCase):
    def test_encode_one_code_point(self):
        for i in range(0x110000):
            if 0xD800 <= i <= 0xDFFF:
                continue
            code_point = chr(i)
            expected = code_point.encode('utf-8')
            output = impl.encode_one_code_point(code_point)
            self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
