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

from splice.distances import EditDistanceCalculator


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


if __name__ == '__main__':
    unittest.main()
