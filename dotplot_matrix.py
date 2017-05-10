import numpy as np


# Create dotplot matrix for two sequences
def dotplot(seqA, seqB, w, s):
    # get the middle of sequence
    mid = w // 2
    # Generate zeros matrix
    dp = np.zeros((len(seqA), len(seqB)), dtype=int)
    len_a = len(seqA)
    len_b = len(seqB)
    # Align the sequences
    for i in range(len_a - w + 1):
        part1 = seqA[i:i + w]
        for j in range(len_b - w + 1):
            part2 = seqB[j:j + w]
            counter = 0
            for k in range(w):
                if part1[k] == part2[k]:
                    counter += 1
            # Fill the matrix
            if counter >= s:
                dp[i + mid, j + mid] = 1
    return dp
