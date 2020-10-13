# https://www.youtube.com/watch?v=Wkx0fI4e0fs

NUCLEOTIDES_DNA = list('ACGT')
NUCLEOTIDES_RNA = list('ACGU')
NUCLEOTIDES = list(sorted(set(NUCLEOTIDES_DNA).union(NUCLEOTIDES_RNA)))


def is_dna_nucleotide(thing):
    return thing in NUCLEOTIDES_DNA


def is_rna_nucleotide(thing):
    return thing in NUCLEOTIDES_RNA


def is_dna_sequence(seq):
    return all(map(is_dna_nucleotide, seq))


def is_rna_sequence(seq):
    return all(map(is_rna_nucleotide, seq))


def count_nucleotides(seq):
    # `collections.Counter(seq)` is a terrible idea: it doesn't create an entry for missing nucleotides.
    # You can try setting zeros and imposing an order, then using Counter.update or Counter.__add__ but those
    # mess up the order or remove the zeros.  So this may be less optimized but its behavior is much more predictable.
    return {n: seq.count(n) for n in NUCLEOTIDES}


def rosalind_count_dna(histogram):
    return ' '.join(str(histogram[n]) for n in NUCLEOTIDES_DNA)


def transcribe_to_rna(dna):
    try:
        return dna.replace('T', 'U')
    except AttributeError:  # It's not a string.
        pass
    return ('U' if n == 'T' else n for n in dna)
