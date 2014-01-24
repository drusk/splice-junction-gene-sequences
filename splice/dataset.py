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


class GeneSequence(object):
    def __init__(self, name, characters, classification=None):
        self.name = name
        self.characters = characters
        self.classification = classification

    @classmethod
    def parse_line(cls, text):
        classification, name, characters = map(str.strip, text.split(","))
        return cls(name, characters, classification)


class DataSet(object):
    def __init__(self, gene_sequences):
        self.gene_sequences = gene_sequences

    def __len__(self):
        return len(self.gene_sequences)

    @classmethod
    def parse_file(cls, filename):
        with open(filename, "rb") as filehandle:
            return cls([GeneSequence.parse_line(line) for line in filehandle])
