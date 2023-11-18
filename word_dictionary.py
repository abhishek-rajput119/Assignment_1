class WordNode: 
    def __init__(self):
        self.children = dict()
        self.is_end = False

class WordDictionary(object):

    def __init__(self):
        self.root = WordNode()
        
    def addWord(self, word):
        currentNode = self.root
        for letter in word:
            if letter not in currentNode.children.keys():
                currentNode.children[letter] = WordNode()
            currentNode = currentNode.children.get(letter)
        currentNode.is_end = True

    def search(self, word):
        currentNode = self.root
        for index in range(len(word)):
            letter = word[index]
            if letter not in currentNode.children.keys():
                return False, index
            currentNode = currentNode.children.get(letter)
        return currentNode.is_end, len(word)
    
    def _get_all_suggestions(self, node, word, suggested_words):
        if node.is_end:
            suggested_words.append(word)
 
        for value, childNode in node.children.items():
            self._get_all_suggestions(childNode, word + value, suggested_words)
 
    def get_all_suggestions(self, prefix_key):
        currentNode = self.root
 
        for letter in prefix_key:
            if not currentNode.children.get(letter):
                return []
            currentNode = currentNode.children[letter]
 
        if not currentNode.children:
            return []

        suggested_words = list()
        self._get_all_suggestions(currentNode, prefix_key, suggested_words)

        return suggested_words