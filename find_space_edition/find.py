import unittest

def find_repeat(numbers):

    # Find a number that appears more than once
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

        find_repeat(left)
        find_repeat(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] == right[j]:
                return left[i]
            if left[i] < right[j]:
                numbers[k] = left[i]
                # move the iterator forward
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

            while i < len(left):
                numbers[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                numbers[k] = right[j]
                j += 1
                k += 1
                
    for n in range(len(numbers) - 1):
        if numbers[n] == numbers[n+1]:
            return numbers[n]


    return 0


















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
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)