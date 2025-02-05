def wildcard_match(string, pattern):
    """
    Checks if the string matches the pattern with '*' and '?' as wildcards.
    '*' matches zero or more characters.
    '?' matches exactly one character.
    """
    s_len, p_len = len(string), len(pattern)
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    dp[0][0] = True

    # Handle patterns starting with '*'
    for j in range(1, p_len + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if pattern[j - 1] == string[i - 1] or pattern[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[s_len][p_len]


def count_matches_in_file(filename, pattern):
    """
    Reads a file and counts the number of lines that match the given pattern.
    """
    match_count = 0

    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if wildcard_match(line.strip(), pattern):
                    match_count += 1
    except Exception as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)

    return match_count


# Example Usage
if __name__ == "__main__":
    file_name = "example.txt"  # Replace with your filename
    search_pattern = "t*st?"  # Replace with your pattern
    matches = count_matches_in_file(file_name, search_pattern)
    print(f"Number of matches: {matches}")
