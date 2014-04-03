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

import math


class DistanceCalculator(object):
    def _check_same_length(self, sequence1, sequence2):
        if len(sequence1) != len(sequence2):
            raise ValueError("Sequences must have same length.")

    def calculate_distance(self, sequence1, sequence2):
        raise NotImplementedError()


class EditDistanceCalculator(DistanceCalculator):
    def calculate_distance(self, sequence1, sequence2):
        self._check_same_length(sequence1, sequence2)

        count = 0
        for i in xrange(len(sequence1)):
            if sequence1[i] != sequence2[i]:
                count += 1

        return count


class GaussianWeightedDistanceCalculator(DistanceCalculator):
    """
    Gives more weight to nucleotides around the boundary.
    """

    def __init__(self, centre=30, variance=20):
        self.centre = centre
        self.variance = variance

    def calculate_distance(self, sequence1, sequence2):
        self._check_same_length(sequence1, sequence2)

        distance = 0
        for i in xrange(len(sequence1)):
            delta = 0
            if sequence1[i] == sequence2[i]:
                delta = 1

            distance += self._weight(i) * (1 - delta)

        return distance

    def _weight(self, index):
        return math.exp(
            -math.pow(index - self.centre, 2) / self.variance)
