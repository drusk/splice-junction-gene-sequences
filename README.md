splice-junction-gene-sequences
==============================

Analysis of the data set at
http://archive.ics.uci.edu/ml/datasets/Molecular+Biology+%28Splice-junction+Gene+Sequences%29

Goal
----
Recognize, given a sequence of DNA, the boundaries between exons
(the parts of the DNA sequence retained after splicing) and introns
(the parts of the DNA sequence that are spliced out).

Attribute Information
---------------------
1. One of {n ei ie}, indicating the class.
   (ei = exon-intron boundary, ie = intron-exon boundary, n = neither)

2. The instance name.

3-62. The remaining 60 fields are the sequence, starting at position -30
and ending at position +30. Each of these fields is almost always filled
by one of {a, g, t, c}. Other characters indicate ambiguity among the
standard characters.

Data Set
--------
For full details on the data set see docs/dataset_readme.txt

Domain Theory
-------------
See docs/domain_theory.txt
