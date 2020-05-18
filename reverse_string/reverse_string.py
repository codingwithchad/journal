import unittest

# Because python strings are immutable, we split the string into a list of chars
def split(word):
    return [char for char in word]

# Because our goal is to reverse a string, we use the combine function
# to cast the char list back into a string
def combine(char_list):
    str = ""
    for char in char_list:
        str+=char
    return str
# Takes a string reverses the string
def reverse_string(the_string):

    word_length = len(the_string)
    start = 0
    end = word_length - 1
    while start <= end:
        the_string[start], the_string[end] = the_string[end], the_string[start]
        start += 1
        end -= 1
    return the_string



class Test(unittest.TestCase):

    def test_hello_world(self):
        word_as_list = split('hello world')
        actual = combine(reverse_string(word_as_list))
        expected = 'dlrow olleh'
        self.assertEqual(actual, expected)

    def test_race_car(self):
        word_as_list = split('Race car!')
        actual = combine(reverse_string(word_as_list))
        expected = '!rac ecaR'
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)