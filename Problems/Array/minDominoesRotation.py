# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
class Solution:
    '''
    We want to check if all elements in either top or bottom are equal to tops[i] or bottoms[i]
    [2,1,2,4,2,2]
    [5,2,6,2,3,2]
    target = [2,5]
    for 2 -> try to make each number in tops = 2 or try to make each number in bottoms
        by rotating -> if target in bottoms[i], rotation += 1
        rotate only when current side doesn't have target but other side does (for that index)

    '''
    def minDominoRotations(self, tops, bottoms):
        def check(target):
            top_rotation =  bottom_rotation = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target: return -1
                if tops[i] != target:
                    top_rotation += 1
                if bottoms[i] != target:
                    bottom_rotation += 1
            return min(top_rotation, bottom_rotation)
        ans = min(check(tops[0]), check(bottoms[0]))
        return ans if ans else -1

        target1 = tops[0]
        target2 = bottoms[0]
        ans = []
        valid1 = valid2 = valid3 = valid4 = True
        rotation1, rotation2, rotation3, rotation4 = 0, 0, 0, 0
        # make top = target1
        for i in range(len(tops)):
            if tops[i] == target1: continue
            elif bottoms[i] == target1: 
                rotation1 += 1
            else:
                valid1 = False
                break
        # make bottom = target1
        for i in range(len(bottoms)):
            if bottoms[i] == target1: continue
            elif tops[i] == target1: 
                rotation2 += 1
            else:
                valid2 = False
                break
        # make top = target2
        for i in range(len(tops)):
            if tops[i] == target2: continue
            elif bottoms[i] == target2: 
                rotation3 += 1
            else:
                valid3 = False
                break
        for i in range(len(bottoms)):
            if bottoms[i] == target2: continue
            elif tops[i] == target2: 
                rotation4 += 1
            else:
                valid4 = False
                break
        if valid1: ans.append(rotation1)
        if valid2: ans.append(rotation2)
        if valid3: ans.append(rotation3)
        if valid4: ans.append(rotation4)
        return min(ans) if ans else -1

# 2nd solution: much better
def ans(tops, bottoms):
    for i in [tops[0], bottoms[0]]:
        if all(i in d for d in zip(tops, bottoms)):
            ans = max(tops.count(i), bottoms.count(i))
            return len(tops) - ans
    return -1

# 3rd answer: intuitive
def mindomRotation(tops, bottoms):
    INF = 10 ** 10
    best = INF
    for x in range(2):
        if x == 1: # we swap first element
            tops[0], bottoms[0] = bottoms[0], tops[0]

        # make sure top matches
        rotations = x
        for i in range(len(tops)):
            if tops[0] == tops[i]: continue
            if tops[0] == bottoms[i]:
                rotations += 1
                continue
            rotations = INF
        best = min(rotations, best)

        # make sure bottom matches
        rotations = x
        for i in range(len(bottoms)):
            if bottoms[0] == bottoms[i]: continue
            if bottoms[0] == tops[i]:
                rotations += 1
                continue
            rotations = INF
        best = min(rotations, best)

    if best >= INF: return -1
    return best

    # tops match target1, bottoms match target1 or tops match target2, bottoms match target2
    # target1 = tops[0], target2 = bottoms[0]

print(s.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2])) # 2
print(s.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4])) # -1



