# https://leetcode.com/problems/longest-consecutive-sequence/

# Input: nums = [100,4,200,1,3,2]
# Output: 4


class Solution:
    def longestConsecutive(self, arr):
        """
        Finds the start of a sequence
        Counts the sequence forward
        Tracks the max length
            TC -> O(N) single pass
        """
        s = set(arr)  # 100, 4, 200, 1, 3, 2
        answer = 0
        for number in s:
            # Only start counting if it's the start of a sequence
            if number - 1 not in s:  # if no match then answer 1
                current = number
                streak = 1
                while current + 1 in s:
                    current += 1
                    streak += 1
                answer = max(answer, streak)
                # if 101 present -> length++, 102 present -> length++
        return answer


s = Solution()

print(s.longestConsecutive(arr=[100, 4, 200, 1, 3, 2]))


"""
🔍 Dry Run: Input = [100, 4, 200, 1, 3, 2]
Step 1: Create a set for fast lookup:

s = {1, 2, 3, 4, 100, 200}
answer = 0

🧭 Iterate through each number in the set:
🔹 Number = 100
    99 not in set → ✅ start of a new sequence
    current = 100, streak = 1
    101 not in set → end of sequence
    ➡️ answer = max(0, 1) = 1

🔹 Number = 4
    3 is in set → ❌ skip (not start of sequence)

🔹 Number = 200
    199 not in set → ✅ start of a new sequence
    current = 200, streak = 1
    201 not in set → end of sequence
    ➡️ answer = max(1, 1) = 1

🔹 Number = 1
    0 not in set → ✅ start of a new sequence
    current = 1, streak = 1
        2 in set → current = 2, streak = 2
        3 in set → current = 3, streak = 3
        4 in set → current = 4, streak = 4
        5 not in set → end of sequence
        ➡️ answer = max(1, 4) = 4

🔹 Numbers = 2 and 3
    1 and 2 are in set → ❌ skip (not start of sequence)

Final Answer: 4

Longest consecutive sequence is [1, 2, 3, 4]
"""
