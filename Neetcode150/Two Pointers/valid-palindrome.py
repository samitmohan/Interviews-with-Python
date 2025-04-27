# https://leetcode.com/problems/valid-palindrome/

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Convert upper -> lower, remove spaces / non-alphanumeric characters
# Check for palindrome
# Time Complexity -> O(N)

"""
test_string = ""
for i in range(len(s)):
    if s[i].isalnum() is True:  # returns true if all char in string are alphanumeric
        test_string = test_string + s[i]

# convert to lower
test_string = test_string.lower()
# palindrome check
reverse_string = test_string[::-1]
if test_string == reverse_string:
    return True
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = "".join(word.lower() for word in s if word.isalnum())
        return ans[::] == ans[::-1]
