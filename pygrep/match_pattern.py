# def match_pattern(line, pattern):
#     def is_match(text, pat):
#         i, j = 0, 0
#         last_star, last_match = -1, -1

#         while i < len(text):
#             if j < len(pat) and (pat[j] == '?' or pat[j] == text[i]):
#                 i += 1
#                 j += 1
#             elif j < len(pat) and pat[j] == '*':
#                 last_star = j
#                 last_match = i
#                 j += 1
#             elif last_star != -1:
#                 j = last_star + 1
#                 last_match += 1
#                 i = last_match
#             else:
#                 return False

#         while j < len(pat) and pat[j] == '*':
#             j += 1

#         return j == len(pat)

#     words = line.split()
#     for word in words:
#         if is_match(word, pattern):
#             return True
#     return False

# def match_pattern(line, pattern):
#     def is_match(text, pat):
#         i, j = 0, 0
#         last_star, last_match = -1, -1

#         while i < len(text):
#             if j < len(pat) and (pat[j] == '?' or pat[j].lower() == text[i].lower()):
#                 i += 1
#                 j += 1
#             elif j < len(pat) and pat[j] == '*':
#                 last_star = j
#                 last_match = i
#                 j += 1
#             elif last_star != -1:
#                 j = last_star + 1
#                 last_match += 1
#                 i = last_match
#             else:
#                 return False

#         while j < len(pat) and pat[j] == '*':
#             j += 1

#         return j == len(pat)

#     words = line.split()
#     for word in words:
#         if is_match(word, pattern):
#             return True
#     return False

# # Example usage:
# line = "Unix linux which one you choose."
# pattern = "u*x"

# print(match_pattern(line, pattern))  # Output: True


# # Example usage:
# line = "unix is great os. unix was developed in Bell labs."
# pattern = "un*x"

# file = open("unix_text.txt", "r")

# for line in file:
#     if match_pattern(line, pattern):
#         print(line)
# print(match_pattern(line, pattern))  # Output: True

def match_pattern(line, pattern):
    def is_match(text, pat):
        i, j = 0, 0
        last_star, last_match = -1, -1

        while i < len(text):
            if j < len(pat) and (pat[j] == '?' or pat[j].lower() == text[i].lower()):
                i += 1
                j += 1
            elif j < len(pat) and pat[j] == '*':
                last_star = j
                last_match = i
                j += 1
            elif last_star != -1:
                j = last_star + 1
                last_match += 1
                i = last_match
            else:
                return False

        while j < len(pat) and pat[j] == '*':
            j += 1

        return j == len(pat)

    words = line.split()
    for word in words:
        if is_match(word, pattern) and word.lower().startswith(pattern.replace('*', '').replace('?', '').lower()):
            return True
    return False

# Example usage:
line = "Unix linux which one you choose."
pattern = "un*x"

print(match_pattern(line, pattern))  # Output: True

