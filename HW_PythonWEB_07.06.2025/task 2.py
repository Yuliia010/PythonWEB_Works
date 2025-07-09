import unittest

class Number:
    def __init__(self, value=0):
        self.set_value(value)

    def set_value(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        self.value = value

    def get_value(self):
        return self.value

    def to_binary(self):
        return bin(self.value)

    def to_octal(self):
        return oct(self.value)

    def to_hex(self):
        return hex(self.value)



class TestNumber(unittest.TestCase):
    def setUp(self):
        self.num = Number(42)

    def test_get_value(self):
        self.assertEqual(self.num.get_value(), 42)

    def test_set_value(self):
        self.num.set_value(100)
        self.assertEqual(self.num.get_value(), 100)

    def test_to_binary(self):
        self.assertEqual(self.num.to_binary(), '0b101010')

    def test_to_octal(self):
        self.assertEqual(self.num.to_octal(), '0o52')

    def test_to_hex(self):
        self.assertEqual(self.num.to_hex(), '0x2a')

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            Number("not a number")

if __name__ == '__main__':
    unittest.main()
