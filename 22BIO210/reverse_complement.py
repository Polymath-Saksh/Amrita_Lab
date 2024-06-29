def rev_complement(seq):
    rev_seq = seq
    rev_seq = rev_seq.upper()
    for i in range(len(rev_seq)):
        if rev_seq[i] == 'A':
            rev_seq = rev_seq[:i] + 'T' + rev_seq[i+1:]
        elif rev_seq[i] == 'T':
            rev_seq = rev_seq[:i] + 'A' + rev_seq[i+1:]
        elif rev_seq[i] == 'C':
            rev_seq = rev_seq[:i] + 'G' + rev_seq[i+1:]
        elif rev_seq[i] == 'G':
            rev_seq = rev_seq[:i] + 'C' + rev_seq[i+1:]
        else:
            pass
    return rev_seq

if __name__ == '__main__':
    seq = 'ATGATCTCGTAA'
    print('Original sequence: ' + seq)
    print('Reverse Complement: ' +rev_complement(seq))
