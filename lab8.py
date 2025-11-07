def read_fasta(filename):
    """
    Reads a FASTA file and returns a dictionary:
    {header : sequence}
    """
    fasta_dict = {}
    header = None
    seq_chunks = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                # Save previous entry
                if header is not None:
                    fasta_dict[header] = "".join(seq_chunks)

                header = line[1:]  # remove '>'
                seq_chunks = []
            else:
                seq_chunks.append(line)

        # Save last entry when file ends
        if header is not None:
            fasta_dict[header] = "".join(seq_chunks)

    return fasta_dict


def base_percentages(seq):
    """
    Returns the percentage of bases A, T, G, C in a sequence.
    Output example: {'A': 25.0, 'T': 25.0, 'G': 25.0, 'C': 25.0}
    """
    seq = seq.upper()
    length = len(seq)

    return {b: (seq.count(b) / length * 100) for b in "ATGC"}

if __name__ == "__main__":
    # Change this path to your FASTA file location
    fasta_path = r"C:\Users\6292492\Downloads\sequence.fasta"

    # Read FASTA
    fasta = read_fasta(fasta_path)

    # Print results for each entry
    for header, dna_seq in fasta.items():
        print("HEADER:", header)
        print("Sequence (first 100 bases):", dna_seq[:100])
        print("Base Percentages:", base_percentages(dna_seq))
        print()
