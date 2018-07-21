class FreqTable:
    """Take a list of words, then build it into frequency tables for single 
    letters, doubles, and triplets."""

    def __init__(self, words):
        self.singles = dict()
        self.doubles = dict()
        self.triples = dict()

        # Don't care about case; upper is better for legibility
        [self.parse_word(w.upper()) for w in words]

    def parse_word(self, word):
        """Parse word for single letters, doubles, and triplets."""

        l = len(word)
        for i in range(l):
            # Inital testing shows standard python idiom of
            # d[key] = d.get(key, 0) + 1
            # is significantly slower. More testing could be done later.
            if word[i] in self.singles:
                self.singles[word[i]] += 1
            else:
                self.singles[word[i]] = 1

            if i + 1 < l:
                if word[i:i+2] in self.doubles:
                    self.doubles[word[i:i+2]] += 1
                else:
                    self.doubles[word[i:i+2]] = 1

                if i + 2 < l: # Nest if since only valid if previous if is
                    if word[i:i+3] in self.triples:
                        self.triples[word[i:i+3]] += 1
                    else:
                        self.triples[word[i:i+3]] = 1

