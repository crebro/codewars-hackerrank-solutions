def rule30(list_, n):
    conditions = {
        "000": 0,
        "001": 1,
        "010": 1,
        "011": 1,
        "100": 1,
        "101": 0,
        "110": 0,
        "111": 0,
    }

    retList = list_.copy()
    for _ in range(n):
        retList.insert(0, 0)
        retList.append(0)

        currentListCondition = retList.copy()
        for index, item in enumerate(retList):
            rightNeighbour = 0
            leftNeighbour = 0
            if index != 0:
                leftNeighbour = currentListCondition[index - 1]
            if index != len(retList) - 1:
                rightNeighbour = currentListCondition[index + 1]

            retList[index] = conditions[
                f"{leftNeighbour}{currentListCondition[index]}{rightNeighbour}"
            ]
    return retList
