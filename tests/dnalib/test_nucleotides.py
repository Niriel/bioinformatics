from dnalib.nucleotides import \
    A, C, T, G, U, \
    str_to_dna, str_to_rna, seq_to_str, \
    is_dna_nucleotide, is_dna_sequence, \
    is_rna_nucleotide, is_rna_sequence, \
    count_nucleotides, \
    transcribe_to_rna, \
    transcribe_to_dna, \
    complement_dna, reverse_complement_dna


def test_str_to_dna():
    s = 'gaTtACa'
    assert str_to_dna(s) == [G, A, T, T, A, C, A]


def test_str_to_rna():
    s = 'gaUuACa'
    assert str_to_rna(s) == [G, A, U, U, A, C, A]


def test_seq_to_str():
    seq = [G, A, T, U, A, C, A]
    assert seq_to_str(seq) == 'GATUACA'


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
    dna = str_to_dna('ACCCAACT')
    dna_histogram = count_nucleotides(dna)
    assert dna_histogram == {
        'A': 3,
        'C': 4,
        'G': 0,
        'T': 1,
        'U': 0,
    }
    rna = str_to_rna('ACCCAACU')
    rna_histogram = count_nucleotides(rna)
    assert rna_histogram == {
        'A': 3,
        'C': 4,
        'G': 0,
        'T': 0,
        'U': 1,
    }


def test_transcribe_to_rna():
    dna = str_to_dna('GATGGAACTTGACTACGTAAATT')
    rna = str_to_rna('GAUGGAACUUGACUACGUAAAUU')
    assert transcribe_to_rna(dna) == rna


def test_transcribe_to_dna():
    rna = str_to_rna('GAUGGAACUUGACUACGUAAAUU')
    dna = str_to_dna('GATGGAACTTGACTACGTAAATT')
    assert transcribe_to_dna(rna) == dna


def test_complement_dna():
    dna_0 = str_to_dna('gattaca')
    dna_1 = str_to_dna('ctaatgt')
    assert complement_dna(dna_0) == dna_1


def test_reverse_complement_dna():
    dna_0 = str_to_dna('gattaca')
    dna_1 = str_to_dna('tgtaatc')
    assert reverse_complement_dna(dna_0) == dna_1
