def branch_and_bound_cyclopeptide_sequencing(spectrum):
    amino_acid_mass = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
        'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
        'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

    best_peptide = []

    def is_consistent(peptide, spectrum):
        peptide_spectrum = cyclic_spectrum(peptide)
        for mass in peptide_spectrum:
            if mass not in spectrum:
                return False
        return True

    def expand(peptide):
        expanded_peptides = []
        for mass in amino_acid_mass.values():
            expanded_peptide = peptide + [mass]
            expanded_peptides.append(expanded_peptide)
        return expanded_peptides

    def cyclic_spectrum(peptide):
        prefix_mass = [0]
        for mass in peptide:
            prefix_mass.append(prefix_mass[-1] + mass)

        peptide_mass = prefix_mass[-1]
        spectrum = [0]
        for i in range(len(peptide)):
            for j in range(i + 1, len(peptide) + 1):
                spectrum.append(prefix_mass[j] - prefix_mass[i])

                if i > 0 and j < len(peptide):
                    spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))

        spectrum.sort()
        return spectrum

    def score(peptide, spectrum):
        peptide_spectrum = cyclic_spectrum(peptide)
        count = 0
        for mass in peptide_spectrum:
            if mass in spectrum:
                count += 1
                spectrum.remove(mass)
        return count

    def branch_and_bound(peptide, spectrum):
        nonlocal best_peptide

        if sum(peptide) == max(spectrum):
            if score(peptide, spectrum) > score(best_peptide, spectrum):
                best_peptide = peptide
            return

        if not is_consistent(peptide, spectrum):
            return

        for child in expand(peptide):
            branch_and_bound(child, spectrum.copy())

    branch_and_bound([], spectrum)

    return best_peptide

# Example usage:
experimental_spectrum = [0, 71, 101, 103, 128, 129, 199, 200, 204, 227, 230, 265, 266, 269, 299, 307, 323, 355, 356, 386, 388, 413]
result_peptide = branch_and_bound_cyclopeptide_sequencing(experimental_spectrum)

if result_peptide:
    print("Found cyclic peptide matching the experimental spectrum:", result_peptide)
else:
    print("No cyclic peptide found matching the experimental spectrum.")
