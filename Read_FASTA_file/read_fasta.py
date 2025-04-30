def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        current_id = None
        current_seq = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):  # Header line
                if current_id:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]  # Remove '>'
                current_seq = []
            else:  # Sequence line
                current_seq.append(line)
        # Add the last sequence
        if current_id:
            sequences[current_id] = ''.join(current_seq)
    return sequences


