# Spiralize Codewars Solution - Submitted by [Kreation Duwal]
def spiralize(size):
    grid = [
        [
            1
            if row == 0
            or (row == size - 1 and col != 0)
            or col == size - 1
            or (col == 0 and row != 1)
            else 0
            for col in range(size)
        ]
        for row in range(size)
    ]
    if size <= 4:
        return grid
    inSpiral = spiralize(size - 4)
    grid[2][1] = 1
    for row in range(len(inSpiral)):
        for col in range(size - 4):
            grid[2 + row][2 + col] = inSpiral[row][col]

    return grid
