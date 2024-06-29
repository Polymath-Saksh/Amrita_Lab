from collections import Counter

def find_repeating_kmers(k, seq):
    k_mers = [seq[i:i+k] for i in range(len(seq)-k+1)]# list comprehension

    occ = Counter(k_mers)

    repeating_kmers = {key:value for key,value in occu.items() if value>1}

    sorted = dict(sorted(repeating_kmers.items(), key = lambda item:item[1], reverse = True))

    for key, value in sorted.items():
        print(key, value)

    return sorted