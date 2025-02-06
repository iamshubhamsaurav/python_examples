import sys

def wildcard_match(text, pattern):
    """Matches a string with a pattern that includes '*' and '?'."""
    t_len, p_len = len(text), len(pattern)
    dp = [[False] * (p_len + 1) for _ in range(t_len + 1)]
    dp[0][0] = True  # Empty pattern matches empty text

    # Initialize the DP table for patterns starting with *
    for j in range(1, p_len + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, t_len + 1):
        for j in range(1, p_len + 1):
            if pattern[j - 1] == '?' or pattern[j - 1] == text[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[t_len][p_len]

def count_pattern_in_line(line, pattern):
    """Checks if the line contains the pattern (exact matches only)."""
    return pattern in line

def file_contains_match(filename, pattern):
    """
    Checks if the file contains at least one line that matches the pattern.
    Stops scanning and returns True on the first match, otherwise False.
    """
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                stripped_line = line.strip()
                if '*' in pattern or '?' in pattern:  # Use wildcard_match for patterns with wildcards
                    if wildcard_match(stripped_line, pattern):
                        return True  # Match found, stop scanning
                else:  # Use direct matching for normal patterns
                    if count_pattern_in_line(stripped_line, pattern):
                        return True  # Match found, stop scanning
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
    except Exception as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)
    return False  # No match found