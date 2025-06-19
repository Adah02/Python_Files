import class_tasks
from unittest import TestCase

class TestClass(TestCase):

    def test_for_length_of_list(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = 10

        self.assertEqual(actual, class_tasks.length_of_list(items))

    def test_for_sum_of_elements_in_even_index(self):
        item = [1, 4, 3, 1, 5, 2, 7, 1, 9, 3]
        actual = 25

        self.assertEqual(actual, class_tasks.sum_of_elements_in_even_positions(item))

    def test_for_sum_of_elements_in_odd_index(self):
        item = [1, 4, 3, 1, 5, 2, 7, 1, 9, 3]
        actual = 11

        self.assertEqual(actual, class_tasks.sum_of_elements_in_odd_positions(item))

    def test_average_of_list(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = 5.5

        self.assertEqual(actual, class_tasks.average_of_list(items))

