import unittest

def find_repeat(numbers):

    # Find a number that appears more than once
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:

        mid = floor + ((ceiling - floor) // 2)
        left_floor, left_ceiling = floor, mid
        right_floor, right_ceiling = mid + 1, ceiling

        left_range = 0
        for item in numbers:
            if item >= left_floor and item <= left_ceiling:
                left_range += 1

        items_in_left = (left_ceiling - left_floor + 1)

        if left_range > items_in_left:
            # There must be a duplicate in the left range
            # So use the same approach iteratibely on that range
            floor, ceiling = left_floor, left_ceiling
        else:
            # There must be a duplicate in the right range
            floor, ceiling = right_floor, right_ceiling

    # floor and ceiling have converged
    # We found a number that repeats
    return floor


















# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 8, 3, 2, 4, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)




unittest.main(verbosity=2)