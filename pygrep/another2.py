import sys

def count_matches_in_file(filename, pattern):
    def count_pattern_in_line(line, pattern):
        match_count = 0
        i = 0
        while i <= len(line) - len(pattern):
            if wildcard_match(line[i:], pattern):
                match_count += 1
                i += 1  # Always increment to check for overlaps
            else:
                i += 1
        return match_count

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


def find_first_match_in_file(filename, pattern):
    def wildcard_match_first(text, pattern):  # Modified wildcard match for first match
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

    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if wildcard_match_first(line.strip(), pattern):
                    return True
            return False
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}", file=sys.stderr)
        return None
    

res = count_matches_in_file('test.txt', 'bc')
print(res)
x = find_first_match_in_file('hi.txt', 'bc')
print(x)