def count_peptides_of_mass(target_mass):
    # Define the masses of standard amino acids
    amino_acid_masses = {'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147, 'G': 57, 'H': 137, 'I': 113, 'K': 128,
                         'L': 113, 'M': 131, 'N': 114, 'P': 97, 'Q': 128, 'R': 156, 'S': 87, 'T': 101, 'V': 99, 'W': 186, 'Y': 163}

    # Recursive function to generate peptide sequences and count
    def generate_peptides(current_mass, current_sequence):
        nonlocal count
        if current_mass == target_mass:
            count += 1
            return
        elif current_mass > target_mass:
            return

        for amino_acid, mass in amino_acid_masses.items():
            new_mass = current_mass + mass
            new_sequence = current_sequence + amino_acid
            generate_peptides(new_mass, new_sequence)

    # Initialize count
    count = 0

    # Start the generation with an empty sequence
    generate_peptides(0, '')

    return count

# Example usage
target_mass = 200
result = count_peptides_of_mass(target_mass)
print(f"The number of peptides with mass {target_mass} is: {result}")
