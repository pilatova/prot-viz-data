fixed_order = ['human', 'baboon', 'cow', 'dog', 'mouse', 'opossum']

with open('dist.txt', 'r') as f_in, open('dist2.tsv', 'w') as f_out:
    lines = f_in.readlines()
    num_tables = len(lines) // 8
    
    f_out.write('protein_id\t' + '\t'.join([
        f'{fixed_order[i]}-{fixed_order[j]}'
        for i in range(len(fixed_order))
        for j in range(i + 1, len(fixed_order))
    ]) + '\n')

    for table_idx in range(num_tables):
        start = table_idx * 8 + 1
        protein_id = lines[start].strip()
        
        species = []
        matrix = []
        for i in range(6):
            line = lines[start + 1 + i].strip()
            parts = line.split()
            species.append(parts[0])
            row = parts[1:7]
            matrix.append(row)
        
        original_indices = [species.index(s) for s in fixed_order]
        
        distances = []
        for i in range(5):
            for j in range(i + 1, 6):
                row = original_indices[i]
                col = original_indices[j]
                distances.append(matrix[row][col])
        tab = '\t'
        f_out.write(f"{protein_id}\t{tab.join(distances)}\n")