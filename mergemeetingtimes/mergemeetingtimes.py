import unittest

# Sort tuples by start time
# If start time is is less than previous end time
# Then merge the meetings

def merge_ranges(meetings):
    # Sort the meetings by start time
    # Sorting is O(n log n)
    sorted_meetings = sorted(meetings)

    # Merge meeting ranges
    # Start a merged meetings list with the first meeting
    merged_meetings = [sorted_meetings[0]]

    # Look at each subsequent appointment.
    for current_start, current_end in sorted_meetings[1:]:
        # get the values of the latest merged appointment
        latest_start, latest_end = merged_meetings[-1]

        # Check of the latest meeting end time touches or overlaps the current meeting
        # Then write ever the end time with the latest end time
        # Or app the current meeting to the list
        if latest_end >= current_start:
            merged_meetings[-1] = ((latest_start, max(current_end, latest_end)))
        else:
            merged_meetings.append((current_start, current_end))



    return merged_meetings


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)