from collections import defaultdict


class FreqTable:
    """Take a list of words, then build it into frequency tables for single
    letters, doubles, and triplets."""

    def __init__(self, words):
        # defaultdict allows default values; greatly improves performance
        self.singles = defaultdict(int)
        self.doubles = defaultdict(int)
        self.triples = defaultdict(int)

        # Don't care about case; upper is better for legibility
        [self.parse_word(w.upper()) for w in words]

        # Lazily get rid of non-letters. So far they've only come up
        # significantly in the single letters (since we grab all of those)
        keys_to_remove = [k if not k.isalpha() else None for k in self.singles.keys()]
        for k in keys_to_remove:
            self.singles.pop(k, None)

        # Form full dictionary
        self.all = dict(self.triples, **self.doubles)
        # Update is slower so use the presumably smallest dictionary
        self.all.update(self.singles)

        # Calculate actual frequency
        self.total = sum(self.all.values())
        [self.calc_freq(k) for k in self.all.keys()]

    def parse_word(self, word):
        """Parse word for single letters, doubles, and triplets."""

        l = len(word)
        for i in range(l):
            self.singles[word[i]] += 1

            if i + 1 < l:
                self.doubles[word[i:i + 2]] += 1

                if i + 2 < l:  # Nest if since only valid if previous if is
                    self.triples[word[i:i + 3]] += 1

    def calc_freq(self, key):
        self.all[key] = (self.all[key], self.all[key] / self.total)
