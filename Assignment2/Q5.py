# Input: string S ; string T
# Output: the number of subsequences of S equal to T

import numpy as np


def LargestSubsequence(S, T):
    m = len(S)
    n = len(T)
    dp = np.zeros((len(S) + 1, len(T) + 1))

    if m < n:
        return 0

    for i in range(m + 1):
        dp[i][n] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # if i == m - 1:
            #     dp[i][j] = 0
            # if j == n - 1:
            #     dp[i][j] = 1
            if S[i] != T[j]:
                dp[i][j] = dp[i + 1][j]
            if S[i] == T[j]:
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]

    # print(dp)
    return dp[0][0]


S = "babgbag"
T = "bag"
print(LargestSubsequence(S, T))
