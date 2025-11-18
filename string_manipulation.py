
# --- Easy ---

def to_uppercase(input_string):
    """Converts a string to uppercase."""
    upper_string=input_string.upper()
    return upper_string

def to_lowercase(input_string):
    """Converts a string to lowercase."""
    lower_string=input_string.lower()
    return lower_string

def count_char(input_string, char_to_count):
    """Counts the number of times a character appears in a string."""
    pass

# --- Medium ---

def reverse_string(input_string):
    """Reverses a string."""
    reverse=input_string[::-1]
    return reverse


def reverse_sentence(input_string):
    """Reverses the order of words in a sentence."""
    pass

def is_palindrome(input_string):
    """
    Checks if a string is a palindrome.
    Should be case-insensitive and ignore spaces/punctuation.
    """
    reverse_words=input_string[::-1]
    lower_reverse=reverse_words.lower().strip(" ")
    lower_input=input_string.lower().strip(" ")
    if lower_reverse==lower_input:
        return True
    else:
        return False

# --- Hard ---

def is_anagram(string1, string2):
    """
    Checks if two strings are anagrams.
    Should be case-insensitive and ignore spaces.
    """
    # length_string1=string1.len()
    # length_string2=string2.len()
    lower_string1=string1.lower().len().strip(" ")
    lower_string2=string2.lower().len().strip(" ")

    if lower_string1==lower_string2:
        return True
    else:
        return False

def format_date(date_string):
    """
    Converts a date string like "13 november 2025" to "13/11/2025".
    Should handle different capitalizations and month formats.
    """
    months=['january','february','march','april','may','june','july','august','september','october','november','december']
    for months[0] in months:
        return '1'
    for months[1] in months:
        return '2'
    for months[2] in months:
        return '3'
    for months[3] in months:
        return '4'
    for months[4] in months:
        return '5'
    for months[5] in months:
        return '6'
    for months[6] in months:
        return '7'
    for months[7] in months:
        return '8'
    for months[8] in months:
        return '9'
    for months[9] in months:
        return '10'
    for months[10] in months:
        return '11'
    for months[11] in months:
        return '12'
    