import random

from dnalib.nucleotides import \
    A, C, T, G, U, \
    NUCLEOTIDES, \
    NUCLEOTIDES_DNA, \
    NUCLEOTIDES_RNA, \
    is_dna_nucleotide, is_dna_sequence, \
    is_rna_nucleotide, is_rna_sequence, \
    count_nucleotides, \
    transcribe_to_rna, \
    transcribe_to_dna


def test_is_dna_nucleotide():
    assert is_dna_nucleotide(A)
    assert is_dna_nucleotide(C)
    assert is_dna_nucleotide(G)
    assert is_dna_nucleotide(T)
    assert not is_dna_nucleotide(U)


def test_is_rna_nucleotide():
    assert is_rna_nucleotide(A)
    assert is_rna_nucleotide(C)
    assert is_rna_nucleotide(G)
    assert not is_rna_nucleotide(T)
    assert is_rna_nucleotide(U)


def test_is_dna_sequence():
    assert is_dna_sequence('')
    assert is_dna_sequence([])
    assert is_dna_sequence([A, A, G, T, C])
    assert not is_dna_sequence([A, A, G, U, C])
    assert is_dna_sequence('GCATCGATCTGACGTACTCTCTGAGATCATCAG')
    assert not is_dna_sequence('GCATCGATCTGACGTACTCTCTGAGAT CATCAG')  # Space is illegal.
    assert not is_dna_sequence('GCATCGATCTGACGTACTCTCTGAGATcATCAG')  # Lowercase is illegal.
    assert is_dna_sequence(['A', 'C', 'C'])  # Lists of characters are cool.
    assert not is_dna_sequence(['AA', 'CC', 'CT'])  # Lists of strings are confusing so we reject: flatten first.


def test_is_rna_sequence():
    assert is_rna_sequence('')
    assert is_rna_sequence([])
    assert not is_rna_sequence([A, A, G, T, C])
    assert is_rna_sequence([A, A, G, U, C])
    assert is_rna_sequence('GCAUCGAUCUGACGUACUCUCUGAGAUCAUCAG')
    assert not is_rna_sequence('GCAUCGAUCUGACGUACUCUCUGAGAU CAUCAG')  # Space is illegal.
    assert not is_rna_sequence('GCAUCGAUCUGACGUACUCUCUGAGAUcAUCAG')  # Lowercase is illegal.
    assert is_rna_sequence(['A', 'C', 'C'])  # Lists of characters are cool.
    assert not is_rna_sequence(['AA', 'CC', 'CU'])  # Lists of strings are confusing so we reject: flatten first.


def test_count_nucleotides():
    s = 'ACCCGAAGC'
    for seq in [s, list(s)]:  # Must work with strings and lists.
        histogram = count_nucleotides(seq)
        assert histogram == {
            'A': 3,
            'C': 4,
            'G': 2,
            'T': 0,
            'U': 0,
        }


def test_transcribe_to_rna():
    dna = 'GATGGAACTTGACTACGTAAATT'
    rna = 'GAUGGAACUUGACUACGUAAAUU'
    assert transcribe_to_rna(dna) == list(rna)


def test_transcribe_to_dna():
    rna = 'GAUGGAACUUGACUACGUAAAUU'
    dna = 'GATGGAACTTGACTACGTAAATT'
    assert transcribe_to_dna(rna) == list(dna)
