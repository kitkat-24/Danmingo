# A program to analyze letter and cluster frequencies.
#
# William Ruppenthal, July 2018

from freqTable import build_freq_table

# Load dictionary
with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

# Build frequency table
freq_table = build_freq_table(words)
