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

import matplotlib.pyplot as plt

from splice.dataset import DataSet


def main():
    dataset = DataSet.parse_file("data/splice.data")

    total_counts = collections.defaultdict(int)
    for gene_sequence in dataset:
        for char, count in gene_sequence.char_counts.iteritems():
            total_counts[char] += count

    print total_counts
    print sum(total_counts.values())

    plt.bar(range(len(total_counts)), total_counts.values(), align="center")
    plt.xticks(range(len(total_counts)), total_counts.keys())

    plt.show()


if __name__ == "__main__":
    main()
