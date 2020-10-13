import random

from dnalib.nucleotides import NUCLEOTIDES_DNA, is_dna_nucleotide, is_dna_sequence, count_nucleotides, \
    rosalind_count_dna, transcribe_to_rna


def test_is_nucleotide():
    assert is_dna_nucleotide('A')
    assert is_dna_nucleotide('C')
    assert is_dna_nucleotide('T')
    assert is_dna_nucleotide('G')
    assert not is_dna_nucleotide('a')
    assert not is_dna_nucleotide('c')
    assert not is_dna_nucleotide('t')
    assert not is_dna_nucleotide('g')
    assert not is_dna_nucleotide(123)
    assert not is_dna_nucleotide('B')
    assert not is_dna_nucleotide('AA')  # One character only.
    assert not is_dna_nucleotide('AC')  # Make sure we don't have naive `x in 'ACTG'` returning True for substring.


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
    seq = rnd.choices(NUCLEOTIDES_DNA, k=desired_length)
    assert len(seq) == desired_length
    assert is_dna_sequence(seq)


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


def test_rosalind_count():
    s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    assert rosalind_count_dna(count_nucleotides(s)) == '20 12 17 21'


def test_transcribe_to_rna():
    # Should work with strings.
    dna_s = 'GATGGAACTTGACTACGTAAATT'
    rna_s = 'GAUGGAACUUGACUACGUAAAUU'
    assert transcribe_to_rna(dna_s) == rna_s
    # And with iterables.
    dna_l = list('GATGGAACTTGACTACGTAAATT')
    rna_l = list('GAUGGAACUUGACUACGUAAAUU')
    assert list(transcribe_to_rna(dna_l)) == rna_l


def test_rosalind_transcribe_to_rna():
    # Should work with strings.
    dna_s = 'GATGGAACTTGACTACGTAAATT'
    rna_s = 'GAUGGAACUUGACUACGUAAAUU'
    assert transcribe_to_rna(dna_s) == rna_s
    # And with iterables.
    dna_l = list('GATGGAACTTGACTACGTAAATT')
    rna_l = list('GAUGGAACUUGACUACGUAAAUU')
    assert list(transcribe_to_rna(dna_l)) == rna_l
