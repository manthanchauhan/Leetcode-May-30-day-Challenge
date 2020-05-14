class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [None]*26
        self.isL = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        c = word[0]
        
        if self.data[ord(c) - 97] is None:
            self.data[ord(c) - 97] = Trie()
            
        if len(word) == 1:
            self.data[ord(c) - 97].isL = True
            return
        
        self.data[ord(c) - 97].insert(word[1:])
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        c = word[0]
        
        if self.data[ord(c) - 97] is None:
            return False
        
        if len(word) == 1:
            return self.data[ord(c) - 97].isL
        
        return self.data[ord(c) - 97].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        c = prefix[0]
        
        if self.data[ord(c) - 97] is None:
            return False
        
        if len(prefix) == 1:
            return True
        
        return self.data[ord(c) - 97].startsWith(prefix[1:])
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
