class WordReader:
    def __init__(self, file_path, dictionary_instance):
        """
            Initializes a WordReader object with the provided file path and a WordDictionary instance.

            Parameters:
            - file_path (str): The path to the file containing words to be read and added to the dictionary.
            - dictionary_instance (WordDictionary): An instance of the WordDictionary where words will be added.
        """
        self.file_path = file_path
        self.dictionary_instance = dictionary_instance

    def read_words(self):
        """
            Reads words from the specified file and adds them to the associated WordDictionary instance.
            we directly inserting the words to dictionary instead of storing them and return, to save space 
            as file may be very large. 
            If the file is not found, a FileNotFoundError is caught and an appropriate message is printed.
        """
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    word = line.strip()
                    self.dictionary_instance.addWord(word)

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
