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

        
    def process_file(self, words):
        """Given a list of words, build a frequency table and do some simple
        analysis."""

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
            print("{}: {}, {:.3f}%".format(elem[0], elem[1], 100*ft.all[elem[0]][1]))
        # Not gonna like, I'm proud of this line
        total_percent = sum([ft.all[i[0]][1] for i in top_picks])*100
        print("Total percentage covered by top 52 elements: {:.3f}%".format(total_percent))

    def process_dictionary(self):
        """Load the system dictionary and run frequency analysis on it."""

        # Load dictionary
        with open(self.dict_string, 'r') as f:
            words = f.read().splitlines()

        # Process
        self.process_file(words)

    def process_text(self, filename):
        """Load a single .txt file and run frequency analysis on it."""

        # Load file
        with open(filename, 'r') as f:
            words = f.read().splitlines()

        # Process
        self.process_file(words)

    

if __name__ == "__main__":
    start_time = time.time()

    dan = Danmingo()
    #dan.process_dictionary()
    dan.process_text("data/texts/dewey.txt")

    print("--- %s seconds ---" % (time.time() - start_time))
