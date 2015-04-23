class TrieMap(object):

    """A map based on a prefix tree."""

    def __init__(self):
        self.chars = {}
        self.value = None

    def __contains__(self, key):
        trie = self
        for c in key:
            if not c in trie.chars:
                return False
            trie = trie.chars[c]
        return trie._terminates()

    def __setitem__(self, key, value):
        trie = self
        for c in key:
            if not c in trie.chars:
                trie.chars[c] = TrieMap()
            trie = trie.chars[c]
        trie.value = value

    def _terminates(self):
        return self.value is not None

    def by_prefix(self, prefix):
        trie = self
        for c in prefix:
            if not c in trie.chars:
                return []
            trie = trie.chars[c]

        s = [trie]
        while s:
            t = s.pop()
            if t._terminates():
                yield t.value
            for n in t.chars.values():
                s.append(n)

    def __getitem__(self, key):
        trie = self
        for c in key:
            trie = trie.chars[c]
        return trie.value

    def __repr__(self):
        return repr(self.chars)


class TrieSet(object):

    """A set interface over a TrieMap."""

    def __init__(self):
        self.trie = TrieMap()

    def __contains__(self, x):
        return x in self.trie

    def add(self, item):
        self.trie[item] = item
