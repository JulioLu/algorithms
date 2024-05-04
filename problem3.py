import numpy as np


# n is string len, P is of size m where P[i] is the split pos that split string into [1,i] and [i+1,n] (1-based)
def spliting_cost(P, n):
    P = [0] + P + [n]  # make sure pos list contains both ends of string
    m = len(P)
    P = [0] + P  # both C and P are 1-base indexed for easy reading
    C = np.full((m + 1, m + 1), np.inf)
    for i in range(1, m + 1): C[i, i:i + 2] = 0  # any segment <= 2 does not need split so is zero cost
    for s in range(2, m):  # s is split string len
        for i in range(1, m - s + 1):
            j = i + s
            for k in range(i, j + 1):
                C[i, j] = min(C[i, j], P[j] - P[i] + C[i, k] + C[k, j])
    return C[1, m]


print(spliting_cost([10, 18, 19], 20))