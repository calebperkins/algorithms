class TrieMap(object):
    """A map based on a prefix tree"""
    def __init__(self):
        self.chars = {}
    def __contains__(self, key):
        trie = self
        for c in key:
            if not c in trie.chars:
                return False
            trie = trie.chars[c]
        return None in trie.chars
    def __setitem__(self, key, value):
        trie = self
        for c in key:
            if not c in trie.chars:
                trie.chars[c] = TrieMap()
            trie = trie.chars[c]
        trie.chars[None] = value
    def __getitem__(self, key):
        trie = self
        for c in key:
            trie = trie.chars[c]
        return trie.chars[None]
    def __repr__(self):
        return repr(self.chars)

if __name__ == '__main__':
    t = TrieMap()
    assert "hello" not in t
    t["hello"] = "world"
    assert "hello" in t
    assert "hell" not in t
    assert t["hello"] == "world"
    print(t)

