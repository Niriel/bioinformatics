import random
from dnalib.nucleotides import NUCLEOTIDES, is_nucleotide, is_dna_sequence, count_nucleotides


def test_is_nucleotide():
    assert is_nucleotide('A')
    assert is_nucleotide('C')
    assert is_nucleotide('T')
    assert is_nucleotide('G')
    assert not is_nucleotide('a')
    assert not is_nucleotide('c')
    assert not is_nucleotide('t')
    assert not is_nucleotide('g')
    assert not is_nucleotide(123)
    assert not is_nucleotide('B')
    assert not is_nucleotide('AA')  # One character only.
    assert not is_nucleotide('AC')  # Make sure we don't have naive `x in 'ACTG'` returning True for substring.


def test_is_dna_sequence():
    assert is_dna_sequence('')
    assert is_dna_sequence([])
    assert is_dna_sequence('GCATCGATCTGACGTACTCTCTGAGATCATCAG')
    assert not is_dna_sequence('GCATCGATCTGACGTACTCTCTGAGAT CATCAG')  # Space is illegal.
    assert not is_dna_sequence('GCATCGATCTGACGTACTCTCTGAGATcATCAG')  # Lowercase is illegal.
    assert is_dna_sequence(['A', 'C', 'C'])  # Lists of characters are cool.
    assert not is_dna_sequence(['AA', 'CC', 'CT'])  # Lists of strings are confusing so we reject: flatten first.


def test_random_sequence():
    rnd = random.Random('my seed')
    desired_length = 20
    seq = rnd.choices(NUCLEOTIDES, k=desired_length)
    assert len(seq) == desired_length
    assert is_dna_sequence(seq)


def test_count_nucleotides():
    s = 'ACCCGAAGC'
    for seq in [s, list(s)]:  # Must work with strings and lists.
        histogram = count_nucleotides(seq)
        print(histogram)
        assert histogram == {
            'A': 3,
            'C': 4,
            'G': 2,
            'T': 0,
        }
