def generate_theoretical_spectrum(peptide):
    # Dictionary to store the integer masses of amino acids
    amino_acid_mass = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
        'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
        'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

    # Convert the peptide to a list of integer masses
    peptide_masses = [amino_acid_mass[aa] for aa in peptide]

    # Calculate cyclic subpeptides
    cyclic_subpeptides = [peptide]
    for i in range(1, len(peptide)):
        cyclic_subpeptides.append(peptide[i:] + peptide[:i])

    # Calculate masses of subpeptides
    spectrum = [0]
    for subpeptide in cyclic_subpeptides:
        for i in range(len(peptide)):
            for j in range(1, len(peptide)):
                if i + j <= len(peptide):
                    spectrum.append(sum(peptide_masses[i:i + j]))
    # Sort the spectrum
    spectrum.sort()

    return spectrum

# Example usage:
peptide_sequence = "LEQN"
result_spectrum = generate_theoretical_spectrum(peptide_sequence)
print("Theoretical Spectrum:", result_spectrum)
