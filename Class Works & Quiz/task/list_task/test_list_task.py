import list_task
from unittest import TestCase

class MyTestCase(TestCase):

    def test_access_third_element(self):
        check = [1, 2, 8, 4, 5, 6, 7]
        expected = 8
        self.assertEqual(expected, list_task.accessing_third_element(check))  # add assertion here

    def test_change_last_element(self):
        list = ['kit', 8, 4, 6, 7]
        check = 'kitten'
        expected = ['kit', 8, 4, 6, 'kitten']
        self.assertEqual(expected, list_task.changing_last_element(list, check))

    def test_add_item_to_list(self):
        list = ['kit', 8, 4, 6, 7]
        check = 'ball'
        expected = ['kit', 8, 4, 6, 7, 'ball']
        self.assertEqual(expected, list_task.adding_item_to_list(list, check))

    def test_remove_item_from_list(self):
        list = ['kit', 3, 4, 6, 7]
        expected = ['kit', 4, 6, 7]
        self.assertEqual(expected, list_task.removing_third_element(list))

    def test_checking_length_of_elements(self):
        list = ['kit', 'Emma', 'James', 'John']
        expected = [3, 4, 5, 4]
        self.assertEqual(expected, list_task.length_of_elements(list))

    def test_Ascending_list(self):
        list = [4, 3, 1, 5, 2]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected, list_task.ascending_list(list))

    def test_for_even_numbers_in_list(self):
        list = [8, 4, 6, 7, 3, 12, 1]
        expected = [8, 4, 6, 12]
        self.assertEqual(expected, list_task.list_of_even_numbers(list))

    def test_for_extending_list(self):
        a = [8, 4, 6, 7, 3]
        b = ['Emma', 'James']
        expected = [8, 4, 6, 7, 3, 'Emma', 'James']
        self.assertEqual(expected, list_task.combining_list(a, b))

    def test_for_words_greater_than_three(self):
        names = ['Emma', 'two', 'James', 'in', 'eight', 'of']
        expected = ['Emma', 'James', 'eight']
        self.assertEqual(expected, list_task.elements_greater_than_three_in_list(names))
