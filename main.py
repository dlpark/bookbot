def main():
    text_location = "books/frankenstein.txt"
    text = get_text(text_location)
    wordcount = get_wordcount(text)
    charcount = get_char_count(text)

    print(f"Analysing text in the file: {text_location}")
    print(f"This file contains {wordcount} words.")
    print(charcount)

def get_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_wordcount(input_text):
    words = input_text.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_char_count(input_text):
    # Create a dictionary to store the letters and their counts
    letters = {}
    # Convert input text to all lower case to avoid counting letters twice
    text_lowercase = input_text.lower()
    # Check if each letter is in the dictionary and either add to dictionary or increment count
    for letter in text_lowercase:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

main()