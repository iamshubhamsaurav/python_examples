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
    """Count occurrences of the pattern in the line (exact matches only)."""
    match_count = 0
    i = 0
    while i <= len(line) - len(pattern):
        if line[i:i+len(pattern)] == pattern:  # Direct string comparison for exact matches
            match_count += 1
            i += 1
        else:
            i += 1
    return match_count

def count_matches_in_file(filename, pattern):
    """Count lines in a file that match the given pattern."""
    match_count = 0
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                stripped_line = line.strip()
                if '*' in pattern or '?' in pattern:  # Use wildcard_match for patterns with wildcards
                    if wildcard_match(stripped_line, pattern):
                        match_count += 1
                else:  # Use direct matching for normal patterns
                    match_count += count_pattern_in_line(stripped_line, pattern)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        return 0
    except Exception as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)
        return 0

    return match_count




res = count_matches_in_file('test.txt', 'a*c')
print(res)
res = count_matches_in_file('test.txt', 'bc')
print(res)