# Function to generate dotplot text file

def dotplot2Ascii(dp, seqA, seqB, heading, filename):
    with open(filename, 'w') as f:
        f.write(heading + "\n\n |" + seqB + "\n")
        for i in range(len(seqB)):
            if i == 1:
                f.write("+")
            f.write("-")
        f.write("\n")
        for i in range(len(dp)):
            f.write(seqA[i] + "|")
            for j in range(len(dp[0])):
                if dp[i][j] == 0:
                    f.write(" ")
                elif dp[i][j] == 1:
                    f.write("*")
            f.write("\n")
