class WordDictionary(object):

    def __init__(self):
        self.dict = defaultdict(set)
        self.len2word = defaultdict(set)

    def addWord(self, word):

        for i, c in enumerate(word):
            self.dict[(i, c)].add(word)

        self.len2word[len(word)].add(word)

    def search(self, word):
        ans = copy.deepcopy(self.len2word[len(word)])
        for i, c in enumerate(word):
            if c != '.':
                ans &= self.dict[(i, c)]
        return True if len(ans) else False