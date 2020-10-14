A, C, G, T, U = 'A', 'C', 'G', 'T', 'U'
NUCLEOTIDES = [A, C, G, T, U]
NUCLEOTIDES_DNA = [A, C, G, T]
NUCLEOTIDES_RNA = [A, C, G, U]

STR_TO_DNA = {'a': A, 'A': A,
              'c': C, 'C': C,
              'g': G, 'G': G,
              't': T, 'T': T}

STR_TO_RNA = {'a': A, 'A': A,
              'c': C, 'C': C,
              'g': G, 'G': G,
              'u': U, 'U': U}


def str_to_dna(xs):
    return [STR_TO_DNA[x] for x in xs]


def str_to_rna(xs):
    return [STR_TO_RNA[x] for x in xs]


def seq_to_str(seq):
    return ''.join(map(str, seq))


def is_dna_nucleotide(thing):
    return thing in NUCLEOTIDES_DNA


def is_rna_nucleotide(thing):
    return thing in NUCLEOTIDES_RNA


def is_dna_sequence(iterable):
    return all(map(is_dna_nucleotide, iterable))


def is_rna_sequence(iterable):
    return all(map(is_rna_nucleotide, iterable))


def count_nucleotides(seq):
    # `collections.Counter(seq)` is a terrible idea: it doesn't create an entry for missing nucleotides.
    # You can try setting zeros and imposing an order, then using Counter.update or Counter.__add__ but those
    # mess up the order or remove the zeros.  So this may be less optimized but its behavior is much more predictable.
    return {n: seq.count(n) for n in NUCLEOTIDES}


# Transcription rules.
DNA_TO_RNA = {T: U}
RNA_TO_DNA = {U: T}
DNA_COMPLEMENT = {A: T, C: G, G: C, T: A}


def transcribe_nuc(rule, nuc):
    return rule.get(nuc, nuc)


def transcribe_seq(rule, seq):
    return [transcribe_nuc(rule, nuc) for nuc in seq]


def transcribe_to_rna(dna):
    return transcribe_seq(DNA_TO_RNA, dna)


def transcribe_to_dna(rna):
    return transcribe_seq(RNA_TO_DNA, rna)


def complement_dna(dna):
    return transcribe_seq(DNA_COMPLEMENT, dna)


def reverse_complement_dna(dna):
    return transcribe_seq(DNA_COMPLEMENT, reversed(dna))
