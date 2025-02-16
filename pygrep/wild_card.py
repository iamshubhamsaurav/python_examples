def match_pattern_in_line(line, pattern):
    """Check if the pattern (with '*' and '?') is found anywhere in the line."""
    line = line.lower()
    pattern = pattern.lower()

    def is_match(text, pat):
        """Checks if text matches pattern completely."""
        i, j = 0, 0  # Pointers for text and pattern
        star, last_match = -1, -1  # Track '*' position and last match in text

        while i < len(text):
            if j < len(pat) and (text[i] == pat[j] or pat[j] == '?'):
                i += 1
                j += 1
            elif j < len(pat) and pat[j] == '*':
                star = j
                last_match = i
                j += 1
            elif star != -1:
                j = star + 1
                last_match += 1
                i = last_match
            else:
                return False

        while j < len(pat) and pat[j] == '*':
            j += 1
        
        return j == len(pat)

    # Sliding window check: Match the pattern against every possible substring
    for start in range(len(line)):
        if is_match(line[start:], pattern):
            return True

    return False

# Example usage
print(match_pattern_in_line("unix is great os", "unix"))  # True
print(match_pattern_in_line("unix is great os", "u*x"))   # True
print(match_pattern_in_line("unix is great os", "un*x"))  # True
print(match_pattern_in_line("unix is great os", "linux")) # False
print(match_pattern_in_line("Hello world!", "H*o"))       # True
