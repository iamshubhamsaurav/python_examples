def extract_words(text):
    """
    Extract words from the given text.
    
    Args:
        text (str): The text to extract words from.
    
    Returns:
        list: A list of words extracted from the text.
    """
    words = []
    word = ''
    for char in text:
        if char.isalnum():
            word += char
        else:
            if word:
                words.append(word)
                word = ''
    if word:
        words.append(word)
    return words

def match_pattern(word, pattern):
    """Check if a word matches a pattern with '*' and '?' wildcards."""
    word = word.lower()
    pattern = pattern.lower()
    
    i, j = 0, 0  # Pointers for word and pattern
    star, last_match = -1, -1  # Track '*' position and last match in word

    while i < len(word):
        if j < len(pattern) and (word[i] == pattern[j] or pattern[j] == '?'):
            # Direct match or '?' match
            i += 1
            j += 1
        elif j < len(pattern) and pattern[j] == '*':
            # '*' wildcard: store position, assume zero match
            star = j
            last_match = i
            j += 1
        elif star != -1:
            # Backtrack: Try matching '*' to one more character
            j = star + 1
            last_match += 1
            i = last_match
        else:
            # No match
            return False

    # Ensure remaining pattern is only '*'
    while j < len(pattern) and pattern[j] == '*':
        j += 1
    
    return j == len(pattern)


def grep_tool(text, pattern):
    """Counts occurrences of words matching the pattern."""
    words = extract_words(text)  # Extract words properly
    count = sum(1 for word in words if match_pattern(word, pattern))
    
    return count

# Example usage
text = """unix is great os. unix was developed in Bell labs. 

learn operating system.

Unix linux which one you choose.

uNix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful."""

print(grep_tool(text, "unix"))  # Expected Output: 8
print(grep_tool(text, "u*x"))   # Expected Output: 8
print(grep_tool(text, "un*x"))  # Expected Output: 8
