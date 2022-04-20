import math

# Array Manipulation HackerRank Solution - Submitted by [Kreation Duwal]
def arrayManipulation(n, queries):
    v = [0 for i in range(n + 1)]
    for query in queries:
        v[query[0] - 1] += query[2]
        v[query[1]] -= query[2]

    mv = -math.inf
    li = 0
    for item in v[0:-1]:
        val = li + item
        if val > mv:
            mv = val
        li = val

    return mv
