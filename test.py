
board=[
            [0, 0, 0, 0, 7, 0, 0, 8, 0,],
            [2, 7, 4, 9, 0, 8, 0, 0, 5,],
            [0, 0, 5, 0, 1, 0, 2, 7, 0,],
            [0, 0, 0, 4, 0, 0, 0, 6, 7,],
            [0, 0, 2, 0, 8, 0, 0, 5, 4,],
            [7, 4, 0, 5, 0, 0, 9, 0, 0,],
            [5, 0, 9, 1, 4, 0, 0, 0, 8,],
            [3, 0, 1, 8, 9, 0, 0, 4, 2,],
            [0, 8, 0, 3, 0, 2, 1, 9, 6,],
        ]
        
numbers = [n for n in range(1,10)]
def is_valid(i, j, n):
    # Check row, column, and grid for the presence of the number
    return (
        n not in board[i] and
        n not in (board[r][j] for r in range(9)) and
        n not in (
            board[r][c]
            for r in range(3 * (i // 3), 3 * (i // 3) + 3)
            for c in range(3 * (j // 3), 3 * (j // 3) + 3)
        )
    )

def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in numbers:
                    if is_valid(i, j, n):
                        board[i][j] = n
                        if solve():
                            return True
                        board[i][j] = 0
                return False
    return True

solve()
for row in board:
    print(row)
