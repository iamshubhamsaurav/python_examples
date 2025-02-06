import os
import sys

def wildcard_match(text, pattern):
    """Matches a string with a pattern that includes '*' and '?'."""
    t_len, p_len = len(text), len(pattern)
    dp = [[False] * (p_len + 1) for _ in range(t_len + 1)]
    dp[0][0] = True  # Empty pattern matches empty text

    for j in range(1, p_len + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, t_len + 1):
        for j in range(1, p_len + 1):
            if pattern[j - 1] == '?' or pattern[j - 1] == text[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[t_len][p_len]

def search_pattern_in_file(filename, search_pattern):
    """
    Reads a file line by line and prints matching lines with their line numbers.
    """
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            line_number = 0
            for line in file:
                line_number += 1
                stripped_line = line.strip()
                if '*' in search_pattern or '?' in search_pattern:
                    if wildcard_match(stripped_line, search_pattern):
                        print(f"{filename}:{line_number}: {stripped_line}")
                else:
                    if search_pattern in stripped_line:
                        print(f"{filename}:{line_number}: {stripped_line}")
    except Exception as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)

def recursive_search_excluding_files(directory, exclude_pattern, search_pattern):
    """
    Recursively searches for a pattern in all files under a directory,
    but skips files that match the given exclude pattern.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if wildcard_match(file, exclude_pattern):  # Skip files matching the exclude pattern
                continue
            file_path = os.path.join(root, file)
            search_pattern_in_file(file_path, search_pattern)

# Example Usage
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <directory> <exclude_pattern> <search_pattern>", file=sys.stderr)
        sys.exit(1)

    dir_name = sys.argv[1]
    exclude_pattern = sys.argv[2]  # e.g., "*.log" (skip all .log files)
    search_pattern = sys.argv[3]  # The pattern to search within files

    print(f"Searching for '{search_pattern}' in directory '{dir_name}' while skipping files matching '{exclude_pattern}'...")
    recursive_search_excluding_files(dir_name, exclude_pattern, search_pattern)
