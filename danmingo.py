# A program to analyze letter and cluster frequencies.
#
# William Ruppenthal, July 2018

import glob
import operator
import re
import string
import time

from freqTable import FreqTable


class Danmingo:
    def __init__(self):
        # Nothing to do here for now
        self.dict_string = '/usr/share/dict/words'
        self.debug_true = False
        self.regex = re.compile('[^a-zA-Z\s]+')


    def debug(self, msg):
        if self.debug_true:
            print('DEBUG: {}'.format(msg))

    def process(self, words):
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
        # Not gonna lie, I'm proud of this line
        total_percent = sum([ft.all[i[0]][1] for i in top_picks])*100
        print("Total percentage covered by top {} elements: {:.3f}%".format(len(top_picks), total_percent))


    def process_dictionary(self):
        """Load the system dictionary and run frequency analysis on it."""

        # Load dictionary
        with open(self.dict_string, 'r') as f:
            words = f.read().splitlines()

        # Process
        self.process(words)


    def process_single_text(self, filename):
        """Load a single .txt file and run frequency analysis on it."""

        # Load file
        with open(filename, 'r') as f:
            # Strip punctuation and split by word
            words = self.regex.sub('', f.read()).split()

        # Process
        self.process(words)


    def process_text(self, directory):
        """Load all .txt files in a directory and run frequency analysis on
        them."""

        words = []
        for filename in glob.glob('data/texts/*.txt'):
            with open(filename, 'r') as f:
                # Strip punctuation and split by word
                words += self.regex.sub('', f.read()).split()

        self.debug('Loaded all words')

        # Process
        self.process(words)



if __name__ == "__main__":
    start_time = time.time()

    dan = Danmingo()
    dan.debug_true = True
    #dan.process_dictionary()
    dan.process_text("data/texts/dewey.txt")

    print("--- %s seconds ---" % (time.time() - start_time))
