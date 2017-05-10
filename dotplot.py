import sys
from os.path import isfile
from read_file import read_file_app
from ex2 import dotplot
from ex3 import dotplot2Ascii
from ex4 import dotplot2Graphics

extensions = ['txt', 'eps', 'jpeg', 'jpg', 'pdf', 'pgf', 'png', 'ps', 'raw', 'rgba', 'svg', 'svgz', 'tif', 'tiff']


def execute(w, s, seq_a, seq_b, output):
    dp = dotplot(seq_a, seq_b, w, s)
    seq_a = "".join(read_file_app(seq_a)[1:])
    seq_b = "".join(read_file_app(seq_b)[1:])
    if output.split(".")[-1] == extensions[0]:
        dotplot2Ascii(dp, seq_a, seq_b, "Dotplot matrix", output)
    else:
        dotplot2Graphics(dp, "Sequence A", "Sequence B", "Scatter Plot", output)


extension = sys.argv[5].split(".")[-1]
assert extension in extensions
assert sys.argv[1].isdigit()
assert sys.argv[2].isdigit()
assert isfile(sys.argv[3])
assert isfile(sys.argv[4])
w = int(sys.argv[1])
s = int(sys.argv[2])
assert w % 2 == 1
execute(w, s, sys.argv[3], sys.argv[4], sys.argv[5])
