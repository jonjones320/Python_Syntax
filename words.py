def print_upper_words (words, must_start_with):
    """Prints a new list of words, starting with given letters, in all-caps."""

    # The function iterates through the given "starting" letters, capitalizing each letter.
    for letter in must_start_with:
        upper_letter = letter.upper()

        # Then iterates that letter through the list of words, capitalizing each word.
        for word in words:
            upper_word = word.upper()
            if upper_word.startswith(f"{upper_letter}"):
                print(upper_word)