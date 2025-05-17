# https://leetcode.com/problems/open-the-lock/description/
# https://www.youtube.com/watch?v=Pzg3bCDY87w


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            ans = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                ans.append(lock[:i] + digit + lock[i + 1 :])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                ans.append(lock[:i] + digit + lock[i + 1 :])
            return ans

        q = deque()
        q.append(["0000", 0])  # [lock, turns]
        visit = set(deadends)
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns  # answer found
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])  # backtracking solution
        return -1
