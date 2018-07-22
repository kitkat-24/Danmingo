# A program to analyze letter and cluster frequencies.
#
# William Ruppenthal, July 2018

import operator
import time

from freqTable import FreqTable


class Danmingo:
    def __init__(self):
        # Nothing to do here for now
        self.dict_string = '/usr/share/dict/words'

    def process_dictionary(self):
        """Load the system dictionary and run frequency analysis on it."""

        # Load dictionary
        with open(self.dict_string, 'r') as f:
            words = f.read().splitlines()
        
        # Build frequency table
        ft = FreqTable(words)
        
        # By default, will sort in ascending order, which gives us lowest frequency
        # items first (don't want)
        #whole_sorted = sorted(ft.all.items(), key=lambda kv: kv[1], reverse=True)
        non_singles = sorted(list(ft.doubles.items()) + list(ft.triples.items()), 
                             key=lambda kv: kv[1], reverse = True)
        stop = 26 if len(non_singles) >= 26 else len(non_singles)
        top_picks = sorted(list(ft.singles.items()) + list(non_singles[0:stop]),
                           key=lambda tup: tup[1], reverse = True)
        
        for elem in top_picks:
            print("{}: {}".format(elem[0], elem[1]))

    

if __name__ == "__main__":
    start_time = time.time()

    dan = Danmingo()
    dan.process_dictionary()

    print("--- %s seconds ---" % (time.time() - start_time))
