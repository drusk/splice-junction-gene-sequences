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
from mock import Mock

from splice.dataset import DataSet, GeneSequence
from splice.distances import EditDistanceCalculator
from splice.classifiers import NearestNeighboursClassifier


class NearestNeighboursTest(unittest.TestCase):
    def create_gene_sequence(self, classification):
        gene = Mock(spec=GeneSequence)
        gene.classification = classification
        return gene

    def test_k_3(self):
        seq1 = self.create_gene_sequence("IE")
        seq2 = self.create_gene_sequence("EI")
        seq3 = self.create_gene_sequence("IE")
        seq4 = self.create_gene_sequence("N")
        seq5 = self.create_gene_sequence("EI")
        seq6 = self.create_gene_sequence("EI")

        def dist(seq1, seq2):
            distances = {
                seq1: 1,
                seq2: 2,
                seq3: 3,
                seq4: 4,
                seq5: 5,
                seq6: 6
            }
            try:
                return distances[seq1]
            except KeyError:
                return distances[seq2]

        distance_calculator = Mock(spec=EditDistanceCalculator)
        distance_calculator.calculate_distance = Mock(side_effect=dist)

        dataset = DataSet([seq1, seq2, seq3, seq4, seq5, seq6])

        classifier = NearestNeighboursClassifier(dataset,
                                                 distance_calculator,
                                                 k=3)

        assert_that(classifier.classify(GeneSequence("G1", "ABC")),
                    equal_to("IE"))


if __name__ == '__main__':
    unittest.main()
