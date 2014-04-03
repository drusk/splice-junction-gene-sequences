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

import collections
import operator


class NearestNeighboursClassifier(object):
    def __init__(self, training_data, distance_calculator, k=5):
        self.training_data = training_data
        self.distance_calculator = distance_calculator
        self.k = k

    def classify(self, gene_sequence):
        class_distances = []

        for training_gene in self.training_data:
            distance = self.distance_calculator.calculate_distance(
                gene_sequence, training_gene)
            class_distances.append((training_gene.classification, distance))

        sorted_classes = [classification for classification, dist in
                          sorted(class_distances, key=operator.itemgetter(1))]

        nearest_neighbour_classes = sorted_classes[:self.k]

        counter = collections.defaultdict(int)
        for classification in nearest_neighbour_classes:
            counter[classification] += 1

        return max(counter.iterkeys(), key=lambda key: counter[key])
