from dnalib.nucleotides import rosalind_count_dna, count_nucleotides, transcribe_to_rna


def rosalind_01():
    s = 'GGCAGGAACCCTGTCGGCTTCTCCCCCCTATACGGAAAAAAGTGTGGCAGTGGAAGAAAGACCCACTGCGTTCGGAAAAACTAGCGCTCGAACGCTCGGCAGGGTAA' \
        'CGCCTCGGACTGACAGTCTCTAGTATGTCATCCCACAAACCTGACAACGACCCTCCGGGAGAGTCCGAGTCATGAAGGGCGGGCGGCTTTAACAACATCCACTTGCA' \
        'CTGAACGCTTTAGACATGGCTTGATGCGCCAGGCCATTGCAATCTTTCTTTGCACACACATTCAGGTGGTTCTCAGTAACTGTAAACGATGAACGAGGCACGCGGTT' \
        'CATGATGGTTGCGTGGCAGTATAAAAAACTTAAACGTTCGAAAGGGAGATTTGGTTCGCGTCGCCACGTGCGCGGTATGCGGCTAAACGGCAGACGAACATACTCTT' \
        'AGATGCTTTTAGAATCCGGACTAGTATTGCCTGGTATACTGGTGATAGGAGCAGTGCAGTTAGTGTTACCAAAATCACTCACTTCTAAGCCGAGTGTCGGTAAACAG' \
        'CACACATGATATCCATGGGCATATTAGCAAGGTCGGACGGGTACCAAGAAAAGTAAGGTGCGTGCCATCAAATTACTGTTTATCGGGTCAGAGATTCTAATGCATGT' \
        'TGCGAGGCATGTACTCAACTGTCTTGAGTGGCCAGGATTTGAGGTTGACGAGGGCCTGAAAAATTGTGAGCTTGGTGGGAAGAGAGAGAAGGAGGAGTTCTATTCTG' \
        'CATCATGCGGCATCCTCCAGGAGTTCCCGCAATATTTAGTAGGGCGGTCCGGTAGCCCGCTAAGAGACGCCTGAGTGACAGAAATCATGGACGCCCGGCGCGTCACT' \
        'ATTAACTAATTAGCTGCATAAGATCGAGCGGACCGTGACGATAAGATCGAAGATGTGAGCTTTCTAAAACAGTGGGGCGGACTTCACGTTTCGAGCGCTGGGCCA'
    print(rosalind_count_dna(count_nucleotides(s)))


def rosalind_02():
    s = 'AGCAGTGCGGTCTCGGGCCGGCTTGGCTGTCTCGACCGATGTGCGCTCATGCGCGTCGAATGATGATGATACACGTGTTTGACAATTTGTATTCATTAGTTCTGAGC' \
        'GAACATTCGTGACGGCGCGGAGTAGCCGGATTAATACTACGTAGTCCCAGTGGTTCGTCGCGGGAGTCCATCAGCGGCAGATACCCGTAGGAAAGCGCTCGTTACGG' \
        'TTTGGGCATCCCCCAGACATCTCCGCACCCTGGCCAAGTGGGAACGCCCGTGACTCGCCTTCGCTCGTGGAAGAGCGATAGTTTTTGGTTACAGGTTATTGATTCCG' \
        'CATGCACCACGTCCGCTCCACAGAAAGCTTCTACTGCTCGTGCGTTAGACTGCCTCTGGGATGTGACAGATTCGACGGTGACGTAAATGGGACCGCTATAACAAATA' \
        'AGGATTAGATGAGATCCGATCTCGTGCGGACTGATCCGACCTCGCCATCACGGCAAGGAGCTAGCCGTGGTCTCTAGTCCTCCACGATCAGTGTTCAATGTGTTGCG' \
        'GAACGTACTGCGGCCCAAGTCGGTGCGCTTATCGGATTATCGCGCTACCCAAGCTGGTAGTTAGGACCAGGATGGTCATATTCGGTCATACAAGATGATGATACCGC' \
        'AGGCCCAAACCATTCCGATAGAAGCGTAGTCGCGGTGGAGTGCCGTGTACATTCAAGGATCACACGCTGCACATTATATCGCTGAAGCCCACGAAAAAAAATAGCGC' \
        'CCCGGACGTAGCGAGCCGTATGCCATTCCTTTCCGTGTGCTAGCCCCCATGAGTTTAGGTCACTGCCCCCAATCGCGCTTTCAGGCTAGTATCAGTTAAGCCACTAA' \
        'ACGTGGACACCTACTCTGTCACCATCATTGCTTGGAGAGTTAGATGGGGCCAGGAGCAATTAAATATTGCCGCTAGCCACCATTAACACGAGCCTTACTATTTACT'
    print(transcribe_to_rna(s))


if __name__ == '__main__':
    rosalind_02()
