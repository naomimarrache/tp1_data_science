import unittest

from esme_lessons.job_interview.anagrams import anagram


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        # Given
        n = '1234'
        expected_output = 4321
        # When
        output = anagram(n)

        # Then
        self.assertEqaual(expected_output, output)

