import unittest


def sort_scores(unsorted_scores, highest_possible_score):

    # if the length is 0 or 1, we can return. There is nothing to sort.
    if len(unsorted_scores) <= 1:
        return unsorted_scores

    # Create a list to hold all possible scores in O(m) space where m is the size of highest_possible_score
    all_scores = [0] * highest_possible_score

    # For each score in unsorted scores, add it to the all_scores list. this is O(n) time
    # where n is the size of unsorted_scores
    for score in unsorted_scores:
        all_scores[score] += 1

    # sortedscores is a list to hold the scores in sorted order
    sortedscores = []

    # Loop through all the scores in the high score list is O(m) time
    # If there is a score at that number, we add it to the sortedscores list
    for score in range(len(all_scores) - 1, -1, -1):
        if(all_scores[score] > 0):
            for i in range(all_scores[score]):
                sortedscores.append(score)

    return sortedscores

# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)