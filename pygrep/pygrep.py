import sys

def count_matches_in_file(filename, pattern):
    def count_pattern_in_line(line, pattern):
        match_count = 0
        i = 0
        while i <= len(line) - len(pattern):
            if line[i:i+len(pattern)] == pattern: # Direct string comparison for exact matches
                match_count += 1
                i += 1
            else:
                i += 1
        return match_count

    # ... (rest of the file handling code is the same)
    match_count = 0
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                match_count += count_pattern_in_line(line.strip(), pattern)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        return 0
    except Exception as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)
        return 0
    return match_count

def wildcard_match(text, pattern):
    def matches(t_idx, p_idx):
        if p_idx == len(pattern):
            return t_idx == len(text)
        if pattern[p_idx] == '*':
            for i in range(len(text) - t_idx + 1):
                if matches(t_idx + i, p_idx + 1):
                    return True
            return False
        if t_idx < len(text) and (pattern[p_idx] == '?' or pattern[p_idx] == text[t_idx]):
            return matches(t_idx + 1, p_idx + 1)
        return False

    return matches(0, 0)


### testing 

res = count_matches_in_file('test.txt', 'bc')
print(f'Total Matches {res}')

# Example Usage
# if __name__ == "__main__":
#     file_name = "example.txt"  # Replace with your filename
#     search_pattern = "t*st?"  # Replace with your pattern
#     matches = count_matches_in_file(file_name, search_pattern)
#     print(f"Number of matches: {matches}")
