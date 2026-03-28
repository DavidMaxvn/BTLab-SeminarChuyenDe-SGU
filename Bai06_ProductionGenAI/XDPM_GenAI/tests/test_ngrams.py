import unittest

from src.chapter13.ngrams import create_ngrams, lowercase_remove_punct_numbers, multiple_to_single_spaces


class TestLowercaseRemovePunctNumbers(unittest.TestCase):
    def test_mixed_input(self):
        self.assertEqual(lowercase_remove_punct_numbers("Hello, World! 123"), "hello world ")

    def test_lowercase_only(self):
        self.assertEqual(lowercase_remove_punct_numbers("this is a test"), "this is a test")

    def test_empty_string(self):
        self.assertEqual(lowercase_remove_punct_numbers(""), "")

    def test_phone_number_removed(self):
        self.assertEqual(lowercase_remove_punct_numbers("Call me at 123-456-7890"), "call me at ")


class TestSpaceNormalization(unittest.TestCase):
    def test_multiple_spaces(self):
        self.assertEqual(multiple_to_single_spaces("a   b\t\tc\n\n d"), "a b c d")


class TestCreateNgrams(unittest.TestCase):
    def test_create_trigrams(self):
        text = "abcde"
        self.assertEqual(create_ngrams(text, 3), ["abc", "bcd", "cde"])

    def test_short_input(self):
        self.assertEqual(create_ngrams("ab", 3), [])

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            create_ngrams("abc", 0)


if __name__ == "__main__":
    unittest.main()
