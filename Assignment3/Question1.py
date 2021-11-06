# Assign banana to monkeys
# There are N Monkeys and N bananas are placed in a straight line.
# Each monkey want to have a banana, if two monkeys want to own the same banana,
# there will be a fight!A monkey can stay at his position,
# move one step right from x to x + 1, or move one step left from x to x -1.
# Any of these moves consumes 1 second.
# Assign monkeys to banana so that not monkey fight each other and the time
# when the last monkey gets a banana is minimized.
# Input: The input contain two arrays of int. The first array is the positions of monkeys.
# The second array is the positions of bananas.
# The output is a int, which is the time(in seconds) it takes when all bananas are assigned to monkeys.

def Monkeyassignbananas(A, B):
    #  A is the positions of monkeys. B is the positions of bananas.
    n = len(A)
    ans = [0]*n
    for i in range(n):
        ans[i] = abs(B[i] - A[i])
    return max(ans)


# Test
A = [1, 3, 6]
B = [2, 4, 6]
print(Monkeyassignbananas(A, B))
