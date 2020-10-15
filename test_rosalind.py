from dnalib.nucleotides import \
    NUCLEOTIDES_DNA, \
    seq_to_str, \
    str_to_dna, \
    count_nucleotides, \
    transcribe_to_rna, \
    reverse_complement_dna


def rosalind_count_dna(histogram):
    return ' '.join(str(histogram[n]) for n in NUCLEOTIDES_DNA)


def test_rosalind_01():
    dna = str_to_dna('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    histogram = count_nucleotides(dna)
    formated = ' '.join(str(histogram[n]) for n in NUCLEOTIDES_DNA)
    assert formated == '20 12 17 21'


def test_rosalind_02():
    s = 'GATGGAACTTGACTACGTAAATT'
    dna = str_to_dna(s)
    rna = transcribe_to_rna(dna)
    assert seq_to_str(rna) == 'GAUGGAACUUGACUACGUAAAUU'


def test_rosalind_03():
    s = 'AAAACCCGGT'
    dna_forward = str_to_dna(s)
    dna_reverse = reverse_complement_dna(dna_forward)
    assert seq_to_str(dna_reverse) == 'ACCGGGTTTT'
