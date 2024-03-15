def complement(x):
    # return the complement of a base
    # use a dictionary to map each base to its complement
    return {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[x]

def complement_strand(main_strand):
    # return the complement of a DNA strand
    # join the complement of each base in the main strand

    #Step 1: Iterate through the main strand and get the complement of each base
    #Step 2: Join the complement of each base to form the complement strand
    return ''.join(complement(x) for x in main_strand)

if __name__ == '__main__':
    in_strand = input('Enter a DNA strand: ')
    print(f'Complementary DNA strand: {complement_strand(in_strand)}')
