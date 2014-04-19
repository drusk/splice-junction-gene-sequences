# Copyright (C) 2014 David Rusk
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

__author__ = "David Rusk <drusk@uvic.ca>"

import unittest

from hamcrest import assert_that, equal_to

from splice.distances import (EditDistanceCalculator,
                              KnowledgeBasedDistanceCalculator)


class EditDistanceCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = EditDistanceCalculator()

    def test_identical_strings_0_dist(self):
        assert_that(self.calculator.calculate_distance("ABC", "ABC"),
                    equal_to(0))

    def test_char_diffs_counted(self):
        assert_that(self.calculator.calculate_distance("ABC", "ABB"),
                    equal_to(1))
        assert_that(self.calculator.calculate_distance("ABC", "AED"),
                    equal_to(2))
        assert_that(self.calculator.calculate_distance("ABC", "FED"),
                    equal_to(3))

    def test_unequal_length_raises_exception(self):
        self.assertRaises(ValueError,
                          self.calculator.calculate_distance, "ABC", "ABCD")


class KnowledgeBasedDistanceCalculatorTest(unittest.TestCase):
    """
    TODO refactor: repeated offsets
    """

    def setUp(self):
        self.calculator = KnowledgeBasedDistanceCalculator()

    def build_sequence(self, chars, offset, length=60, placeholder="X"):
        seq = placeholder * offset + chars
        return seq + placeholder * (length - len(seq))

    def test_ei_distance_all_same(self):
        offset = 27
        seq1 = self.build_sequence("AAGGTAAGT", offset, placeholder="X")
        seq2 = self.build_sequence("AAGGTAAGT", offset, placeholder="Y")

        assert_that(self.calculator.ei_distance(seq1, seq2), equal_to(0))

    def test_ei_distance_equiv_chars(self):
        offset = 27
        seq1 = self.build_sequence("AAGGTAAGT", offset, placeholder="X")
        seq2 = self.build_sequence("CAGGTGAGT", offset, placeholder="Y")

        assert_that(self.calculator.ei_distance(seq1, seq2), equal_to(0))

    def test_ei_distance_some_differences(self):
        offset = 27
        seq1 = self.build_sequence("AAGGTAAGT", offset, placeholder="X")
        seq2 = self.build_sequence("CCGTTGGGT", offset, placeholder="Y")

        assert_that(self.calculator.ei_distance(seq1, seq2), equal_to(3))

    def test_ie_distance_all_same(self):
        offset = 20
        seq1 = self.build_sequence("CCCCCCACAGGG", offset, placeholder="X")
        seq2 = self.build_sequence("CCCCCCACAGGG", offset, placeholder="Y")

        assert_that(self.calculator.ie_distance(seq1, seq2), equal_to(0))

    def test_ie_diff_in_27_ignored(self):
        offset = 20
        seq1 = self.build_sequence("CCCCCCACAGGG", offset, placeholder="X")
        seq2 = self.build_sequence("CCCCCCTCAGGG", offset, placeholder="Y")

        assert_that(self.calculator.ie_distance(seq1, seq2), equal_to(0))

    def test_ie_distance_equiv_chars(self):
        offset = 20
        seq1 = self.build_sequence("CCCCCCACAGGG", offset, placeholder="X")
        seq2 = self.build_sequence("TTTTTTATAGGT", offset, placeholder="Y")

        assert_that(self.calculator.ie_distance(seq1, seq2), equal_to(0))

    def test_ie_distance_some_differences(self):
        offset = 20
        seq1 = self.build_sequence("CCCCCCACAGGG", offset, placeholder="X")
        seq2 = self.build_sequence("TTTTTTAGTTGT", offset, placeholder="Y")

        assert_that(self.calculator.ie_distance(seq1, seq2), equal_to(3))


if __name__ == '__main__':
    unittest.main()
