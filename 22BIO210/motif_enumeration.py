def motif_enumeration(dna_list, k, d):
    patterns = set()
    for i in range(len(dna_list[0]) - k + 1):
        kmer = dna_list[0][i:i+k]
        neighbors = neighbors_of_kmer(kmer, d)
        for neighbor in neighbors:
            if is_motif(neighbor, dna_list, k, d):
                patterns.add(neighbor)
    return patterns

def neighbors_of_kmer(kmer, d):
    if d == 0:
        return [kmer]
    if len(kmer) == 1:
        return ['A', 'C', 'G', 'T']
    neighbors = []
    suffix_neighbors = neighbors_of_kmer(kmer[1:], d)
    for suffix in suffix_neighbors:
        if hamming_distance(kmer[1:], suffix) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighbors.append(nucleotide + suffix)
        else:
            neighbors.append(kmer[0] + suffix)
    return neighbors

def hamming_distance(pattern1, pattern2):
    distance = 0
    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            distance += 1
    return distance

def is_motif(pattern, dna_list, k, d):
    for dna in dna_list:
        found = False
        for i in range(len(dna) - k + 1):
            kmer = dna[i:i+k]
            if hamming_distance(pattern, kmer) <= d:
                found = True
                break
        if not found:
            return False
    return True
