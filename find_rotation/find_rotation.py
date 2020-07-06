import unittest


def find_rotation_point(words):

    # Find the rotation point in the list

    floor_index = 0
    floor_word = words[floor_index]
    ceiling_index = len(words) - 1
    mid = 1
    if words[mid - 1] > words[mid]:
        return mid



    while floor_index < ceiling_index:

        guess_index = floor_index + ((ceiling_index - floor_index) // 2)

        if words[guess_index] >= floor_word:
            floor_index = guess_index
        else:
            ceiling_index = guess_index

        if floor_index + 1 == ceiling_index:
            return ceiling_index

    return 0


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)