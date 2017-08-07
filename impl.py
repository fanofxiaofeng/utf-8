#!/usr/local/bin/python3


def encode_one_code_point(cp):
    order = ord(cp)
    # in range [0x0, 0x7F]
    if order < 0x80:
        return order.to_bytes(1, byteorder='big')
    # in range [0x80, 0x7FF]
    elif order < 0x800:
        result = (0xC0 + order // 64).to_bytes(1, byteorder='big')
        return result + ((0x80 + (order % 64)).to_bytes(1, byteorder='big'))
    # in range [0x800, 0xFFFF]
    elif order < 0x10000:
        b1 = (0xE0 + order // 4096).to_bytes(1, byteorder='big')
        b2 = (0x80 + (order % 4096) // 64).to_bytes(1, byteorder='big')
        b3 = (0x80 + (order % 64)).to_bytes(1, byteorder='big')
        return b1 + b2 + b3
    else:
        assert order < 0x200000
        b1 = (0xF0 + order // (2 ** 18)).to_bytes(1, byteorder='big')
        b2 = (0x80 + (order % (2 ** 18)) // 4096).to_bytes(1, byteorder='big')
        b3 = (0x80 + (order % 4096) // 64).to_bytes(1, byteorder='big')
        b4 = (0x80 + (order % 64)).to_bytes(1, byteorder='big')
        return b1 + b2 + b3 + b4
