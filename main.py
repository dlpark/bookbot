def main():
    text_location = "books/frankenstein.txt"
    text = get_text(text_location)
    wordcount = get_wordcount(text)
    char_count = get_char_count(text)
    ordered_char = get_char_order(char_count)

    print(f"--- Analysing text in the file: {text_location} ---")
    print(f"This file contains {wordcount} words.")
    
    for x in range(len(ordered_char)):
        character = ordered_char[x]["character"]
        count = ordered_char[x]["count"]
        print(f"The letter '{character}' appears {count} times.")
    
    print("--- End of analysis ---")

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

def sort_on(dict):
    return dict["count"]

def get_char_order(char_dict):
    # Create a list to store dictionaries
    sorted_char_list = []
    # Iterate through key-value pairs of dictionary items and make each into its own dictionary in the list
    for char, count in char_dict.items():
        entry = {'character': char, 'count': count}
        if char.isalpha():
            sorted_char_list.append(entry)
    # Sort the list by reverse count order
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list   

main()