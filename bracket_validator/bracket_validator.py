import unittest

OPENERS = ['[', '{', '(']
CLOSERS = [']', '}', ')']


def is_open_bracket(char):
    if char in OPENERS:
        return True
    return False

def is_closed_bracket(char):
    if char in CLOSERS:
        return True
    return False


def check_match(opener, bracket):
    if opener == OPENERS[0] and bracket != CLOSERS[0]:
        return False
    elif opener == OPENERS[1] and bracket != CLOSERS[1]:
        return False
    elif opener == OPENERS[2] and bracket != CLOSERS[2]:
        return False
    return True


def is_valid(code):

    # Determine if the input code is valid
    stack = []
    for bracket in code:
        if is_open_bracket(bracket):
            stack.append(bracket)
        elif is_closed_bracket(bracket):
            try:
                opener = stack.pop()
            except IndexError as e:
                return False
            if not check_match(opener, bracket):
                return False

    if len(stack) > 0:
        return False
    return True


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)