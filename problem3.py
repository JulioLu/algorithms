import numpy as np

def spliting_cost(P, n):
    P = [0] + P + [n]
    m = len(P)
    P = [0] + P
    C = np.full((m + 1, m + 1), np.inf)
    for i in range(1, m + 1):
        C[i, i:i + 2] = 0

    for s in range(2, m):
        for i in range(1, m - s + 1):
            j = i + s
            for k in range(i, j + 1):
                C[i, j] = min(C[i, j], P[j] - P[i] + C[i, k] + C[k, j])
    return C[1, m]


string = "abcdabcdabcdabcdabcd"
print("Length of string:", len(string))
print("Minimum splitting cost:", spliting_cost([10, 18, 19], len(string)))
