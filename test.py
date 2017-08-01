#!/usr/local/bin/python3

import impl
import unittest

class Test(unittest.TestCase):
    def testOneCodePoint(self):
        for i in range(0x110000):
            if 0xD800 <= i <= 0xDFFF:
                continue
            codePoint = chr(i)
            expected = codePoint.encode('utf-8')
            output = impl.encode(codePoint)
            # print(expected)
            # print(output)
            self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
