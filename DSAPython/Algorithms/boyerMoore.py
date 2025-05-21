# Boyer-Moore is a string searching algorithm that is based on two main ideas:
# the bad character rule and the good suffix rule.

"""
The boyer_moore function takes two arguments, the text string and the pattern string. It returns the index of the first occurrence of the pattern string in the text string, or -1 if the pattern string is not found.
The function starts by initializing the variables n and m to the lengths of the text and pattern strings respectively. It then checks if the length of the pattern string is greater than the length of the text string, in which case it returns -1.
The skip list is used to store the number of characters to skip when a mismatch occurs. The list is initialized to the length of the pattern string for each character in the ASCII character set. The skip list is constructed by iterating over the characters in the pattern string, and setting the value in the skip list for that character to be the distance from the end of the pattern string to the last occurrence of that character in the pattern string.
The skip list is converted to a tuple to improve performance, since tuples are more memory efficient than lists.
The main loop of the function starts by setting the variable i to the index of the last character in the pattern string. It then enters an inner loop that compares the characters in the text and pattern strings, starting from the end of the pattern string and working backwards. If the characters match, the loop continues until either the beginning of the pattern string is reached, in which case the pattern has been found, or a mismatch is found.
If a mismatch is found, the i variable is incremented by the maximum of the value in the skip list for the mismatched character in the text string, and the number of characters remaining in the pattern string after the mismatched character. This takes into account both the bad character rule and the good suffix rule.
If the pattern string is not found, the function returns -1.
"""
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m > n:
        return -1
    skip = [m] * 256
    for i in range(m - 1):
        skip[ord(pattern[i])] = m - i - 1
    skip = tuple(skip)
    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(skip[ord(text[i])], m - j)
    return -1


text = "ABAAABCD"
pattern = "ABC"
print(boyer_moore(text, pattern))  # Output: 4
