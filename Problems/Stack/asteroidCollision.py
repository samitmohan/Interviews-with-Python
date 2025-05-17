# https://leetcode.com/problems/asteroid-collision/

"""
O(N) time and space
only if a < 0 and stack[-1] > 0 : collision takes place.
  and if a + stack[-1] < 0 : then negative asteroid wins so stack.pop()
      elif a + stack[-1] > 0 : then positive asteroid wins : ignore a (don't add in the stack)
      else a == stack[-1] : both asteroids explore : a = 0 and stack.pop()
"""


def asteroidCollision(asteroids):
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:  # collision takes place
            if a + stack[-1] < 0:
                stack.pop()
            elif a + stack[-1] > 0:
                a = 0  # comes out of the loop
            else:
                stack.pop()
                a = 0
        if a:  # if a still present just add to stack : valid
            stack.append(a)
    return stack


def main():
    print(asteroidCollision([5, 10, -5]))


main()
