# https://www.youtube.com/watch?v=Wkx0fI4e0fs

NUCLEOTIDES = list('ACGT')


def is_nucleotide(thing):
    return thing in NUCLEOTIDES


def is_dna_sequence(seq):
    return all(map(is_nucleotide, seq))


def count_nucleotides(seq):
    # `collections.Counter(seq)` is a terrible idea: it doesn't create an entry for missing nucleotides.
    # You can try setting zeros and imposing an order, then using Counter.update or Counter.__add__ but those
    # mess up the order or remove the zeros.  So this may be less optimized but its behavior is much more predictable.
    return {n: seq.count(n) for n in NUCLEOTIDES}
