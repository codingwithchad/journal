import unittest


def swap_word(word, word_start, word_end):
    while word_start < word_end:
        word[word_start], word[word_end] = word[word_end], word[word_start]
        word_start += 1
        word_end -= 1

def reverse_words(message):
    # Decode the message by reversing the words
    if not message.__contains__(" "):
        return message
    start = 0
    end = len(message)-1
    swap_word(message, start, end)

    word_start = 0
    word_end = 0
    for c in message:
        if word_end >= len(message) - 1:
            swap_word(message, word_start, word_end)
            break
        if c == " ":
            swap_word(message, word_start, word_end - 1)
            word_start = word_end + 1
        word_end += 1


# Tests
class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
