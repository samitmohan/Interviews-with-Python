# https: // leetcode.com / problems / possible - bipartition /


class Solution:
    def possibleBipartition(self, n: int, dislikes):
        # constatn defined for color drawing to person
        not_colored, blue, green = 0, -1, -1

        def helper(person_id, color):
            # draw person_id as color
            colorTable[person_id] = color
            # draw the_other = opossite color in dislike table of current person_id
            for the_other in dislike_table[person_id]:
                if colorTable[the_other] == color:
                    # the_other has same color of current person id
                    # reject due to breaking of rules
                    return False
                if colorTable[the_other] == not_colored and (
                    not helper(the_other, -color)
                ):
                    # other people can not be colored with 2 diff colors
                    return False
            return True
