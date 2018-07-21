# A program to analyze letter and cluster frequencies.
#
# William Ruppenthal, July 2018

import freqTable
import time
start_time = time.time()

# Load dictionary
with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

# Build frequency table
freq_table = freqTable.FreqTable(words)
print(freq_table.singles)
#print(freq_table.doubles)
#print(freq_table.triples)

print("--- %s seconds ---" % (time.time() - start_time))
