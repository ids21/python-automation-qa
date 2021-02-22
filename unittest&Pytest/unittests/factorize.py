import unittest


def factorize(x):
    primfac = []
    if (x == 1):
        return (1,)
    if (x == 0):
        return (0,)
    d = 2
    while d * d <= x:
        while (x % d) == 0:
            primfac.append(d)
            x //= d
        d += 1
    if x > 1:
        primfac.append(x)
    return tuple(primfac)


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ['string', 1.5]
        for x_ in cases:
            with self.subTest(x=x_):
                self.assertRaises(TypeError, factorize, x_)

    def test_negative(self):
        cases = [-1, -10, -100]
        for x_ in cases:
            with self.subTest(x=x_):
                self.assertRaises(ValueError, factorize, x_)

    def test_zero_and_one_cases(self):
        cases = [0, 1]
        results = [(0,), (1,)]
        for idx, x_ in enumerate(cases, start=0):
            with self.subTest(x=x_):
                self.assertEqual(factorize(x_), results[idx])

    def test_simple_numbers(self):
        cases = [3, 13, 29]
        results = [(3,), (13,), (29,)]
        for idx, x_ in enumerate(cases, start=0):
            with self.subTest(x=x_):
                self.assertEqual(factorize(x_), results[idx])

    def test_two_simple_multipliers(self):
        cases = [6, 26, 121]
        results = [(2, 3), (2, 13), (11, 11)]
        for idx, x_ in enumerate(cases, start=0):
            with self.subTest(x=x_):
                self.assertEqual(factorize(x_), results[idx])

    def test_many_multipliers(self):
        cases = [1001, 9699690]
        results = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for idx, x_ in enumerate(cases, start=0):
            with self.subTest(x=x_):
                self.assertEqual(factorize(x_), results[idx])


if __name__ == "__main__":
    unittest.main()