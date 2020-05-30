import unittest

# Helper function as to not repeat code
def one_order_empty(order, served):
    for i in range(len(served)):
        if i > len(order) - 1 or not served[i] == order[i]:
            return False
    return True

# O(n) time, because the longest list is iterated through once,
# 0(1) space, because no new lists are created.
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # Check if we're serving orders first-come, first-served
    if not take_out_orders and not dine_in_orders:
        if not served_orders:
            return True
        else:
            return False
    if len(served_orders) != (len(take_out_orders) + len(dine_in_orders)):
        return False
    if not take_out_orders:
        return one_order_empty(dine_in_orders, served_orders)
    if not dine_in_orders:
        return one_order_empty(take_out_orders, served_orders)

    dinein_count = 0
    takeout_count = 0

    for served in served_orders:
        if served != dine_in_orders[dinein_count] and served != take_out_orders[takeout_count]:
            return False
        if dinein_count < (len(dine_in_orders) - 1) and served == dine_in_orders[dinein_count]:
           dinein_count += 1
        elif takeout_count < (len(take_out_orders) - 1) and served == take_out_orders[takeout_count]:
           takeout_count += 1



    return True


# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_one_register_bad_order(self):
        result = is_first_come_first_served([], [2, 3], [2, 3, 6])
        self.assertFalse(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)


unittest.main(verbosity=2)