class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode ... z
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root # initially start at root
        for c in word:
            if c not in curr.children:   # char is not in hash map
                curr.children[c] = TrieNode() # how we insert characters, use char as key value and create empty trie node
            curr = curr.children[c] # update curr and move to that character, continue with for loop
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):

            curr = root
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        return dfs(0, self.root)










