# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4ed8

def atm_queue(T):
    for t in range(1, T + 1):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))

        # Create a list of tuples (i, A[i]) for each person in the queue
        queue = [(i, a) for i, a in enumerate(A)]

        # Initialize the result list and the current amount withdrawn
        result = []
        withdrawn = 0

        # Keep processing the queue until everyone has left
        while queue:
            # Find the next person to withdraw money
            next_person = queue.pop(0)

            # If they need more money than X, put them at the end of the queue
            if next_person[1] > X:
                queue.append((next_person[0], next_person[1] - X))
            else:
                # Otherwise, they can withdraw all their money and leave the queue
                withdrawn += next_person[1]
                result.append(next_person[0] + 1)

        # Output the result for this test case
        print("Case #{}: {}".format(t, " ".join(str(x) for x in result)))


# Read the number of test cases and call the function to solve the problem
T = int(input())
atm_queue(T)
