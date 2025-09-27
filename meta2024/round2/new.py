def process_case(R, C, K, grid):
    N = R * C
    # Compute total number of ordered pairs
    total_pairs = N * (N - 1)
    # Compute total number of same-owner pairs
    owner_counts = {}
    for row in grid:
        for owner in row:
            owner_counts[owner] = owner_counts.get(owner, 0) + 1
    total_same_owner_pairs = sum(n * (n - 1) for n in owner_counts.values())
    total_diff_owner_pairs = total_pairs - total_same_owner_pairs

    # For each possible Chebyshev distance d, compute total number of ordered pairs at that distance
    Dmax = max(R, C) - 1
    total_pairs_at_d = [0] * (Dmax + 1)  # index 0 to Dmax

    for delta_i in range(R):
        for delta_j in range(C):
            if delta_i == 0 and delta_j == 0:
                continue
            cnt = (R - delta_i) * (C - delta_j)
            if delta_i != 0 and delta_j != 0:
                cnt *= 2  # Positions with delta_i and delta_j swapped
            d = max(delta_i, delta_j)
            total_pairs_at_d[d] += cnt

    # Multiply by 2 to account for ordered pairs
    total_ordered_pairs_at_d = [cnt * 2 for cnt in total_pairs_at_d]

    # Compute the fraction of different-owner pairs
    if total_pairs == 0:
        fraction_diff_owner = 0
    else:
        fraction_diff_owner = total_diff_owner_pairs / total_pairs

    # Calculate the number of different-owner pairs at each distance
    diff_owner_pairs_at_d = [cnt * fraction_diff_owner for cnt in total_ordered_pairs_at_d]

    # Find the K-th smallest score
    cumulative = 0
    for d in range(1, Dmax + 1):
        cumulative += diff_owner_pairs_at_d[d]
        if cumulative + 1e-6 >= K:
            return d
    # If not found, return the maximum distance
    return Dmax

def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        T_line = ''
        # Skip empty lines and read the number of test cases
        while not T_line.strip():
            T_line = infile.readline()
        T = int(T_line)
        for case_num in range(1, T + 1):
            # Read R, C, and K
            while True:
                line = infile.readline()
                if not line.strip():
                    continue
                else:
                    break
            R_C_K = line.strip().split()
            while len(R_C_K) < 3:
                R_C_K.extend(infile.readline().strip().split())
            R, C, K = map(int, R_C_K)
            # Read the grid
            grid = []
            for _ in range(R):
                row = []
                while len(row) < C:
                    line = infile.readline()
                    row.extend(map(int, line.strip().split()))
                grid.append(row[:C])
            # Process the case and get the result
            result = process_case(R, C, K, grid)
            # Write the result to the output file
            outfile.write(f"Case #{case_num}: {result}\n")

# Example usage:
# main('input.txt', 'output.txt')