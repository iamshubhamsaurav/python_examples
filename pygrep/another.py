import os
import sys
import argparse
import time

VERSION = "1.0.0"

def wildcard_match(string, pattern):
    """Match a string against a pattern with '*' and '?' wildcards."""
    s_len, p_len = len(string), len(pattern)
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    dp[0][0] = True  # Empty string matches empty pattern

    # Handle patterns starting with *
    for j in range(1, p_len + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if pattern[j - 1] == '?' or pattern[j - 1] == string[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[s_len][p_len]

def grep_file(pattern, file_path, count=False, line_number=False):
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_no, line in enumerate(file, start=1):
                if wildcard_match(line.strip(), pattern):
                    if count:
                        matches.append(1)
                    elif line_number:
                        matches.append(f"{line_no}: {line.strip()}")
                    else:
                        matches.append(line.strip())
        return matches
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return []

def grep_recursive(root_dir, pattern, include=None, exclude=None, **kwargs):
    results = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if exclude and wildcard_match(filename, exclude):
                continue
            if include and not wildcard_match(filename, include):
                continue
            file_path = os.path.join(dirpath, filename)
            matches = grep_file(pattern, file_path, **kwargs)
            if matches:
                results[file_path] = matches
    return results

def main():
    parser = argparse.ArgumentParser(description="pygrep - A Python implementation of grep.")
    parser.add_argument("pattern", help="The pattern to search for (supports wildcards * and ?).")
    parser.add_argument("files", nargs="*", help="Files or directories to search.")
    parser.add_argument("-c", "--count", action="store_true", help="Print the count of matching lines.")
    parser.add_argument("-i", "--files-with-matches", action="store_true", help="Print file names with matches.")
    parser.add_argument("-n", "--line-number", action="store_true", help="Prefix matches with line numbers.")
    parser.add_argument("-r", "-R", "--recursive", action="store_true", help="Recursively search directories.")
    parser.add_argument("--include", help="Only search files matching this pattern.")
    parser.add_argument("--exclude", help="Skip files matching this pattern.")
    parser.add_argument("-V", "--version", action="store_true", help="Print the version and exit.")
    parser.add_argument("--test", action="store_true", help="Run unit tests.")
    parser.add_argument("--benchmark", action="store_true", help="Run benchmarks.")
    args = parser.parse_args()

    if args.version:
        print(f"pygrep version {VERSION}")
        sys.exit(0)

    if args.test:
        print("Running unit tests...")
        # Placeholder for test functionality
        sys.exit(0)

    if args.benchmark:
        print("Running benchmarks...")
        start_time = time.time()
        # Placeholder for benchmark functionality
        print(f"Benchmark completed in {time.time() - start_time:.2f} seconds.")
        sys.exit(0)

    if not args.pattern:
        print("Error: Pattern is required.", file=sys.stderr)
        sys.exit(1)

    if not args.files:
        print("Error: At least one file or directory is required.", file=sys.stderr)
        sys.exit(1)

    for file_or_dir in args.files:
        if os.path.isdir(file_or_dir) and args.recursive:
            results = grep_recursive(file_or_dir, args.pattern, args.include, args.exclude, 
                                     count=args.count, line_number=args.line_number)
            for file, matches in results.items():
                if args.files_with_matches:
                    print(file)
                elif args.count:
                    print(f"{file}: {sum(matches)}")
                else:
                    for match in matches:
                        print(f"{file}: {match}")
        elif os.path.isfile(file_or_dir):
            matches = grep_file(args.pattern, file_or_dir, count=args.count, line_number=args.line_number)
            if args.files_with_matches and matches:
                print(file_or_dir)
            elif args.count:
                print(f"{file_or_dir}: {sum(matches)}")
            else:
                for match in matches:
                    print(f"{file_or_dir}: {match}")
        else:
            print(f"Error: {file_or_dir} is not a valid file or directory.", file=sys.stderr)

if __name__ == "__main__":
    main()
