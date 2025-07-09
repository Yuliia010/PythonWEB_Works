import unittest

class NumberSet:
    def __init__(self, numbers):
        if not all(isinstance(n, int) for n in numbers):
            raise ValueError("All elements must be integers")
        self.numbers = numbers

    def get_sum(self):
        return sum(self.numbers)

    def get_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def get_max(self):
        return max(self.numbers)

    def get_min(self):
        return min(self.numbers)


class TestNumberSet(unittest.TestCase):
    def setUp(self):
        self.ns = NumberSet([1, 2, 3, 4, 5])

    def test_sum(self):
        self.assertEqual(self.ns.get_sum(), 15)

    def test_average(self):
        self.assertEqual(self.ns.get_average(), 3.0)

    def test_max(self):
        self.assertEqual(self.ns.get_max(), 5)

    def test_min(self):
        self.assertEqual(self.ns.get_min(), 1)


    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            NumberSet([1, "two", 3])

if __name__ == '__main__':
    unittest.main()
