import unittest

# Return the kth to last node in the linked list
def kth_to_last_node(k, head):
    # Raise a value error if k is less than 1.
    if k < 1:
        raise ValueError('k needs to be greater than 1')

    # Create a left and right node, so measure the distance to the end.
    left_node = head
    right_node = head

    # Move the right_node to k nodes away from left_node
    for _ in range(k-1):

        # If k is greater than the length of the list, we will raise an error here.
        if not right_node.next:
            raise ValueError('we fell off the right edge of the list')
        right_node = right_node.next

    # With the left node starting at head
    # Move the right node and left node together
    # Until there is no more right_node.next.
    # Then the left node is k from the end
    while right_node.next:
        right_node = right_node.next
        left_node = left_node.next

    # if there is no right_node.next,
    # Left node will be at the kth node. 
    return left_node




















# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_list_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)


unittest.main(verbosity=2)