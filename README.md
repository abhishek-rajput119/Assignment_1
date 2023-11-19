```markdown
# Trie-based Dictionary Project

This project implements a dictionary data structure using a trie.
The main functionalities include inserting words into the dictionary,
searching for words, and suggesting correct words in case of typos.

## Files

- `main.py`: The main script to run the command line application.
- `word_dictionary.py`: Contains the implementation of the trie-based WordDictionary data structure.
- `word_reader.py`: Implements WordReader, a class for reading words from a text file and adding them to the WordDictionary.

## Getting Started

To run the command line application, use the following command:

```bash
python main.py
```

Before running the application, make sure to install the required packages listed in `requirements.txt`. You can install them using:

```bash
pip install -r requirements.txt
```

## Functionality

### WordDictionary (`word_dictionary.py`)

- `addWord(word)`: Inserts a word into the trie.
- `search(word)`: Searches for a word in the trie and returns a boolean indicating whether the word is found.
- `get_all_suggestions(prefix)`: Retrieves a list of suggested words based on the given prefix.

### WordReader (`word_reader.py`)

- `read_words()`: Reads words from a specified text file and adds them to the WordDictionary.

## Example Usage

1. Run the command line application:

```bash
python main.py
```

2. Enter words for insertion or search according to the prompts.

3. The application will provide suggestions if a searched word contains a typo.

## Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
```
