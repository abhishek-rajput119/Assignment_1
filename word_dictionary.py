class WordNode:
    def __init__(self):
        """
            Initializes a WordNode object, representing a node in the trie structure.
            Each node has a dictionary to store its children nodes and a flag 'is_end' 
            to indicate whether the node marks the end of a word.
        """
        self.children = dict()
        self.is_end = False

class WordDictionary(object):
    def __init__(self):
        """
            Initializes a WordDictionary object with a root WordNode.
            The root serves as the starting point for the trie structure.
        """
        self.root = WordNode()
        
    def addWord(self, word):
        """
            Adds a word to the trie structure represented by the WordDictionary.

            Parameters:
            - word (str): The word to be added to the trie.
            
            Time Complexity:
            - O(n) where n is the length of the word.
            
            Space Complexity:
            - Worst Case: O(n) where n is the length of the word.
            - Best Case: O(m) where m is the (length of word - the number of characters already present in the trie).
        """
        currentNode = self.root
        for letter in word:
            if letter not in currentNode.children.keys():
                currentNode.children[letter] = WordNode()
            currentNode = currentNode.children.get(letter)
        currentNode.is_end = True

    def search(self, word):
        """
            Searches for a word in the trie structure.

            Parameters:
            - word (str): The word to be searched in the trie.

            Returns:
            - tuple (bool, int): A tuple containing a boolean indicating whether 
            the word is found and an integer representing the index up to which
            the word is matched in the trie.
            
            Time Complexity:
            - O(n) where n is the length of the word.

            Space Complexity:
            - O(1)
        """
        currentNode = self.root
        for index in range(len(word)):
            letter = word[index]
            if letter not in currentNode.children.keys():
                return False, index
            currentNode = currentNode.children.get(letter)
        return currentNode.is_end, len(word)
    
    def _get_all_suggestions(self, node, word, suggested_words):
        """
            This is a helper function intended for internal use.
            Recursively retrieves all suggestions (words) from a given node in the trie.

            Parameters:
            - node (WordNode): The starting node for suggestion retrieval.
            - word (str): The current partial word being formed during the recursive traversal.
            - suggested_words (list): A list to store the suggested words. 

            Time Complexity:
            - O(26^L) where 26 is the total number of alphabets in english(as only lower case).
                      L is the (length of longest word - length of prefix).
                      Time complexity may be huge but we could use selective approach to reduce it.
            Space Complexity:
            -worst case -- O(26^L) where 26 is the total number of alphabets in english(as only lower case).
                                            L is the (length of longest word - length of prefix).
       """
        if node.is_end:
            suggested_words.append(word)
 
        for value, childNode in node.children.items():
            self._get_all_suggestions(childNode, word + value, suggested_words)
 
    def get_all_suggestions(self, prefix_key):
        """
            Retrieves all words in the trie that have the given prefix.

            Parameters:
            - prefix_key (str): The prefix for which suggestions are sought.

            Returns:
            - list: A list of suggested words with the given prefix.
        """
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
