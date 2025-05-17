# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

# https://leetcode.com/problems/car-fleet/description/
# More explanation : https://www.youtube.com/watch?v=Pr6T-3yB9RM


# T = D/S : Target - DistOfCar / Speed.
# pairs : (3,3), (5,2), (7,1)  (in sorted order)
#   for 7 : Time : 3 seconds
#   for 5 : Time : 2.5 seconds
#     clearly 5 will reach before 7 hence they will collide and become a fleet (which one to delete : 5 because it will merge will bigger val 7)
#   for 3 : Time : 2.7 seconds
#     3 will reach before 7 also and it will collide and form fleet with 7
#   stack at the end : 7
#   return len(stack)

# Traverse in reverse sorted order : less chances of error since 3 collides with 5 but what if 5 already colliding with 7

# Time : O(N*logN)
# Space : O(N)


def carFleet(target, position, speed):
    pairs = [[pos, sp] for pos, sp in zip(position, speed)]
    stack = []
    for pos, sp in sorted(pairs)[::-1]:  # Reverse sorted order
        time = (target - pos) / sp
        stack.append(time)
        # can only collide if there are 2 elements in stack and if time of stack[-1] is lesser than time of stack[-2]
        # does it overlap?
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


def main():
    target = 10
    position = [3, 5, 7]
    speed = [3, 2, 1]
    print(carFleet(target, position, speed))


main()
