# www.leetcode.com/problems/naming-a-company/description/

from collections import defaultdict


def distinctNmaes(ideas):
    # map key to prefix (c : offee, d : onuts, t : ime, offee)
    hm = defaultdict(set)  # hashset as the value (for uniquely identifying)
    for word in ideas:
        hm[word[0]].add(word[1:])

    ans = 0
    # intersection
    for char1 in hm:
        for char2 in hm:
            if char1 == char2:
                continue  # if same then no answer
            intersect = 0
            for w in hm[char1]:
                if w in hm[char2]:
                    intersect += 1

            # distinct letters (length - intersection)
            d1 = len(hm[char1]) - intersect
            d2 = len(hm[char2]) - intersect
            ans += d1 * d2
    return ans


def main():
    ideas = ["coffee", "donuts", "time", "toffee"]
    print(distinctNmaes(ideas))


main()
