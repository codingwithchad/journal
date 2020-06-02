import unittest


class WordCloudData(object):

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words(input_string)

    def populate_words(self, istring):
        # iterate over each character in the input string, splitting words and
        # passing them to add_to_dictionary
        word_start = 0
        word_len = 0
        for i, char in enumerate(istring):
            # if we reached the end of the string, we check if the last char is a letter
            # then add the last word to the dictionary
            if i == len(istring) - 1:
                if char.isalpha():
                    word_len += 1
                if word_len > 0:
                    current_word = istring[word_start:word_start + word_len]
                    self.add_word_to_dictionary(current_word)

            elif char == ' ' or char == '\u2014':
                if word_len > 0:
                    current_word = istring[word_start:word_start + word_len]
                    self.add_word_to_dictionary(current_word)
                    word_len = 0

            elif char == ".":
                if i < len(istring) - 1 and istring[i+1] == '.':
                    if word_len > 0:
                        current_word = istring[word_start: word_start + word_len]
                        self.add_word_to_dictionary(current_word)
                        word_len = 0

            elif char.isalpha() or char == '\'':
                if word_len == 0:
                    word_start = i
                word_len += 1

            elif char == '-':
                if i > 0 and istring[i-1].isalpha() and istring[i+1].isalpha():
                    if word_len == 0:
                        word_start = i
                    word_len += 1

            else:
                if word_len > 0:
                    current_word = istring[word_start:word_start + word_len]
                    self.add_word_to_dictionary(current_word)
                    word_len = 0

    def add_word_to_dictionary(self, word):
        # If the word is already in the dictionary, increment the word
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1
        # If a lowercase version is in the dictionary
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]
        else:
            self.words_to_counts[word] = 1





    def removeChar(self, theString):
        theString = theString.replace("...", " ")
        removeChar = ["- ", ".", "!", ",", "?"]
        for char in removeChar:
            theString = theString.replace(char, "")
        return theString



# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)