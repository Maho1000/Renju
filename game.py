BOARD_SIZE = 19

def check_winner(board):
    directions = [
        (0, 1),    # горизонтально 
        (1, 0),    # вертикально 
        (1, 1),    # діагональ
        (-1, 1)    # діагональ
    ]

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:
                continue
            color = board[row][col]
            for dr, dc in directions:
                coords = [(row, col)]
                r, c = row + dr, col + dc

                # Збираємо послідовні координати того ж кольору
                while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == color:
                    coords.append((r, c))
                    if len(coords) > 5:
                        break
                    r += dr
                    c += dc

                # Перевірка на точність саме 5 каменів
                if len(coords) == 5:
                    pr = row - dr
                    pc = col - dc
                    nr = r
                    nc = c
                    # Перевіряємо, чи нема каменів до або після
                    if (0 <= pr < BOARD_SIZE and 0 <= pc < BOARD_SIZE and board[pr][pc] == color) or \
                       (0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == color):
                        continue

                    # Найверхніший або найлівіший камінь для відповіді
                    coords.sort()
                    top_left = coords[0]
                    return color, top_left[0] + 1, top_left[1] + 1

    return 0, -1, -1


def parse_input(file_path):
    with open(file_path, "r") as f:
        t = int(f.readline())
        cases = []
        for _ in range(t):
            board = []
            for _ in range(BOARD_SIZE):
                line = f.readline().strip()
                row = list(map(int, line.split()))
                if len(row) != BOARD_SIZE:
                    raise ValueError(f"Expected {BOARD_SIZE} numbers in row, got {len(row)}")
                board.append(row)
            cases.append(board)
    return cases


def write_output(file_path, results):
    with open(file_path, "w") as f:
        for result in results:
            winner, r, c = result
            f.write(f"{winner}\n")
            if winner:
                f.write(f"{r} {c}\n")


def main():
    boards = parse_input("input.txt")
    results = [check_winner(board) for board in boards]
    write_output("output.txt", results)


if __name__ == "__main__":
    main()
