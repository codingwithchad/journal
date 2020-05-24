import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    my_list_len = len(my_list)
    alices_list_len = len(alices_list)
    combine_list = []
    my_count = 0
    alice_count = 0
    combine_count = 0
    if my_list_len == 0 and alices_list_len == 0:
        return []
    if alices_list_len == 0:
        return my_list
    if my_list_len == 0:
        return alices_list

    while my_count < my_list_len and alice_count < alices_list_len:
        if alice_count >= alices_list_len:
            break
        if my_list[my_count] == alices_list[alice_count]:
            combine_list.append(my_list[my_count])
            alice_count +=1
            my_count += 1

        elif my_list[my_count] < alices_list[alice_count]:
            combine_list.append(my_list[my_count])
            my_count += 1
        else:
            combine_list.append(alices_list[alice_count])
            alice_count +=1
        combine_count += 1

    while alice_count < alices_list_len:
        combine_list.append(alices_list[alice_count])
        alice_count += 1
        combine_count += 1
    while my_count < my_list_len:
        combine_list.append(my_list[my_count])
        my_count += 1
        combine_count += 1
    return combine_list


# Tests
class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)

    def test_lists_second_longer(self):
        actual = merge_lists( [1, 7], [2, 4, 6, 8])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)