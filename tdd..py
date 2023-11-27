import itertools

def sequential_word_generation(chars, min_length, max_length):
    wordlist = []
    for length in range(min_length, max_length + 1):
        for word in itertools.product(chars, repeat=length):
            wordlist.append(''.join(word))
    return wordlist

def leetspeak_substitution(word):
    leetspeak_map = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '$',
        't': '7',
    }
    return ''.join(leetspeak_map.get(c.lower(), c) for c in word)

def generate_wordlist(base_word, theme_option, add_prefix, add_suffix):
    variations = []

    if theme_option == 1:
        variations.extend([
            base_word.lower(),
            base_word.upper(),
            base_word.capitalize(),
        ])
    elif theme_option == 2:
        variations.append(leetspeak_substitution(base_word))

    if add_prefix:
        prefix = input("Enter the prefix to add: ")
        variations = [prefix + word for word in variations]

    if add_suffix:
        suffix = input("Enter the suffix to add: ")
        variations = [word + suffix for word in variations]

    return variations

def save_wordlist(wordlist, filename):
    with open(filename, "w") as file:
        for word in wordlist:
            file.write(word + "\n")

if __name__ == "__main__":
    chars = 'abcdefghijklmnopqrstuvwxyz'

    try:
        min_length = int(input("Enter the minimum word length: "))
        max_length = int(input("Enter the maximum word length: "))
    except ValueError:
        print("Invalid input. Please enter valid integer values for word lengths.")
        exit(1)

    print("Choose a theme for the wordlist:")
    print("1. Normal variations (lowercase, uppercase, capitalized)")
    print("2. Leetspeak variations")

    try:
        theme_option = int(input("Enter the number of the theme option: "))
    except ValueError:
        print("Invalid input. Please enter a valid option number.")
        exit(1)

    add_prefix = input("Do you want to add a prefix? (y/n): ").lower() == 'y'
    add_suffix = input("Do you want to add a suffix? (y/n): ").lower() == 'y'

    base_word = input("Enter the base word: ")

    wordlist = sequential_word_generation(chars, min_length, max_length)
    variations = generate_wordlist(base_word, theme_option, add_prefix, add_suffix)

    full_wordlist = wordlist + variations

    output_filename = "wordlist.txt"
    save_wordlist(full_wordlist, output_filename)

    print(f"Wordlist generated and saved to {output_filename}!")
