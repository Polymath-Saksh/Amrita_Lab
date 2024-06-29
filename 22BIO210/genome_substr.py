def translate_codon(codon):
    codon_table = {
        'A': ['GCT', 'GCC', 'GCA', 'GCG'],
        'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'N': ['AAT', 'AAC'],
        'D': ['GAT', 'GAC'],
        'C': ['TGT', 'TGC'],
        'Q': ['CAA', 'CAG'],
        'E': ['GAA', 'GAG'],
        'G': ['GGT', 'GGC', 'GGA', 'GGG'],
        'H': ['CAT', 'CAC'],
        'I': ['ATT', 'ATC', 'ATA'],
        'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'K': ['AAA', 'AAG'],
        'M': ['ATG'],
        'F': ['TTT', 'TTC'],
        'P': ['CCT', 'CCC', 'CCA', 'CCG'],
        'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
        'T': ['ACT', 'ACC', 'ACA', 'ACG'],
        'W': ['TGG'],
        'Y': ['TAT', 'TAC'],
        'V': ['GTT', 'GTC', 'GTA', 'GTG'],
        '*': ['TAA', 'TAG', 'TGA']
    }
    for amino_acid, codon_list in codon_table.items():
        if codon in codon_list:
            return amino_acid
    return None

def find_encoding_substrings(dna, peptide):
    peptide_length = len(peptide)
    substrings = []
    
    for i in range(len(dna) - peptide_length * 3 + 1):
        current_codon = dna[i:i + peptide_length * 3]
        translated_peptide = ''.join([translate_codon(current_codon[j:j + 3]) for j in range(0, len(current_codon), 3)])
        
        if translated_peptide == peptide:
            substrings.append(dna[i:i + peptide_length * 3])
    
    return substrings


dna_sequence = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
amino_acid_sequence = "MA"

result = find_encoding_substrings(dna_sequence, amino_acid_sequence)
print("Substrings encoding the given amino acid sequence:", result)
