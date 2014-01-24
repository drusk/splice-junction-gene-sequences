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

import testutil
from splice.dataset import DataSet, GeneSequence


class DataSetTest(unittest.TestCase):
    def test_parse_gene_sequence(self):
        gene_sequence = GeneSequence.parse_line(
            "EI,    ATRINS-DONOR-521,               CCAGCTGCATCACAGGAGGCCAGCGAGCAGGTCTGTTCCAAGGGCCTTCGAGCCAGTCTG")

        assert_that(gene_sequence.name, equal_to("ATRINS-DONOR-521"))
        assert_that(gene_sequence.classification, equal_to("EI"))
        assert_that(gene_sequence.characters,
                    equal_to("CCAGCTGCATCACAGGAGGCCAGCGAGCAGGTCTGTTCCAAGGGCCTTCGAGCCAGTCTG"))

    def test_parse_dataset(self):
        dataset = DataSet.parse_file(testutil.path("splice.small"))

        assert_that(len(dataset), equal_to(10))
        assert_that(dataset.gene_sequences[0].name, equal_to("ATRINS-DONOR-521"))
        assert_that(dataset.gene_sequences[-1].name, equal_to("GCRHBBA1-DONOR-1590"))

    def test_character_frequencies(self):
        gene_sequence = GeneSequence("1", "CCAGCTGCAT")

        assert_that(gene_sequence.char_counts,
                    equal_to({
                        "A": 2,
                        "C": 4,
                        "G": 2,
                        "T": 2
                    }))


if __name__ == '__main__':
    unittest.main()
