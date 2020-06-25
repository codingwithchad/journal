import unittest

'''
Write a function that, given a sentence , along with the position of an opening parenthesis, 
finds the corresponding closing parenthesis.
'''
def get_closing_paren(sentence, opening_paren_index):
    # ()()((()()))', 5
    # Find the position of the matching closing parenthesis
    count = 0
    for pos in range(opening_paren_index + 1, len(sentence)):
        char = sentence[pos]

        if char == '(':
            count += 1
        elif char == ')':
            if count == 0:
                return pos
            count -= 1

    raise Exception













# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)

    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)