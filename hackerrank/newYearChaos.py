# Minimum Bribes HackerRank solution - Submitted by [Kreation Duwal]
def minimumBribes(q, main=True):
    def protectedPrint(value, condition):
        if condition:
            print(value)

    n = 0
    i = 0

    bribes = {}
    # op is a bool to check if something is outof place
    op = False
    while i < len(q):
        if i != len(q) - 1 and q[i] > q[i + 1]:
            q[i], q[i + 1] = q[i + 1], q[i]
            bribes[q[i + 1]] = bribes[q[i + 1]] + 1 if q[i + 1] in bribes else 1
            if bribes[q[i + 1]] >= 3:
                protectedPrint("Too chaotic", main)
                return
            n += 1
        elif q[i] != i + 1:
            op = True

        i += 1

    if op:
        mb = minimumBribes(q, main=False)
        if not (mb):
            protectedPrint("Too chaotic", main)
            return
        protectedPrint(n + mb, main)
        return n + mb
    protectedPrint(n, main)
    return n
