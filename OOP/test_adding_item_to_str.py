import adding_item_to_str
from unittest import TestCase


class TestAddItemToStr(TestCase):
    def test_that_function_add_item_to_str_of_even_length(self):
        add = adding_item_to_str
        self.assertEqual('helceloo', add.add_item_to_str("helloo", ''))

    def test_add_item_to_empty_string(self):
        add = adding_item_to_str
        self.assertEqual("ce", add.add_item_to_str("", ''))

    def test_that_function_add_item_to_str_of_odd_length(self):
        add = adding_item_to_str
        self.assertEqual("joyce", add.add_item_to_str("joy", ''))