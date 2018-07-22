# A program to analyze letter and cluster frequencies.
#
# William Ruppenthal, July 2018

import operator
import time

from freqTable import FreqTable

start_time = time.time()

# Load dictionary
with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

# Build frequency table
freq_table = FreqTable(words)
#print(freq_table.singles)
#print(freq_table.doubles)
#print(freq_table.triples)

# By default, will sort in ascending order, which gives us lowest frequency
# items first (don't want)
whole_sorted = sorted(freq_table.all.items(), key=lambda kv: kv[1], reverse=True)
for i in range(52):
    print("{}: {}".format(whole_sorted[i][0], whole_sorted[i][1]))
    

print("--- %s seconds ---" % (time.time() - start_time))
