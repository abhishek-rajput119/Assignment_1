from word_dictionary import WordDictionary
from word_reader import WordReader
from fuzzywuzzy import process

if __name__ == "__main__":
    
    file_path = "sd 1 list.txt"
    dictionary = WordDictionary()
    loader = WordReader(file_path, dictionary)
    loader.read_words()
    
    print("Welcome to the word search application")
    print("PRESS CTRL + C to quit")

    while True:
        print("\nEnter the word to search [or type 'EXIT'(case sensitive) to quit]: ")
        searched_word = input().strip()

        if searched_word == 'EXIT':
            break 

        result, index = dictionary.search(searched_word)
        if result:
            print(f"Found the word: {searched_word}")
        else:
            print(f"Sorry, can't find the word '{searched_word}'!")

            if index > 0:
                prefix = searched_word[:index - 1]
                
                suggestions = dictionary.get_all_suggestions(prefix)

                if suggestions:
                    filtered_suggestions = [ratio[0] for ratio in process.extract(query=searched_word, choices=suggestions, limit=3)]
                    print(f"Did you mean? : {', '.join(filtered_suggestions)}")
                else:
                    print("No suggestions available.")
