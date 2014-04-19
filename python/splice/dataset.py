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
import random


class GeneSequence(object):
    def __init__(self, name, characters, classification=None):
        self.name = name
        self.characters = characters
        self.classification = classification

    def __len__(self):
        return len(self.characters)

    def __getitem__(self, item):
        return self.characters[item]

    @property
    def char_counts(self):
        counts = collections.defaultdict(int)
        for char in self.characters:
            counts[char] += 1

        return counts

    @classmethod
    def parse_line(cls, text):
        classification, name, characters = map(str.strip, text.split(","))
        return cls(name, characters, classification)


class DataSet(object):
    def __init__(self, gene_sequences):
        self.gene_sequences = gene_sequences

    def __iter__(self):
        return iter(self.gene_sequences)

    def __len__(self):
        return len(self.gene_sequences)

    @classmethod
    def parse_file(cls, filename):
        with open(filename, "rb") as filehandle:
            return cls([GeneSequence.parse_line(line) for line in filehandle])

    def train_test_split(self):
        genes_by_class = collections.defaultdict(list)

        for gene_sequence in self.gene_sequences:
            genes_by_class[gene_sequence.classification].append(gene_sequence)

        def shuffle_split(sequences):
            split_point = len(sequences) / 2
            random.shuffle(sequences)
            return sequences[:split_point], sequences[split_point:]

        all_training = []
        all_testing = []
        for sequences in genes_by_class.values():
            training, testing = shuffle_split(sequences)
            all_training.extend(training)
            all_testing.extend(testing)

        return DataSet(all_training), DataSet(all_testing)
