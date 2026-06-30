class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False  # mark node as end of word (char)

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root # initially start at root
        for c in word:
            if c not in curr.children:   # char is not in hash map
                curr.children[c] = TrieNode() # how we insert characters, use char as key value and create empty trie node
            curr = curr.children[c] # update curr and move to that character, continue with for loop
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord # if it's true, then it found the entire word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c] # shift curr pointer to child pointer and continue on 
        return True # if we reach end, we know we've found a prefix









        