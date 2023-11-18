class WordReader:
    def __init__(self, file_path, dictionary_instance):
        self.file_path = file_path
        self.dictionary_instance = dictionary_instance

    def read_words(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    word = line.strip()
                    self.dictionary_instance.addWord(word)

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")

