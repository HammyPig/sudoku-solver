def insert_number(value, board, row, col):
    row -= 1
    col -= 1
    board[row][col] = value


def print_board(board):
    i = 0
    for i in range(len(board)):
        # print horizontal separator every 3 rows
        if i % 3 == 0:
            print(25 * "-")

        for j in range(len(board[i])):
            # print vertical separator every 3 columns
            if j % 3 == 0:
                print("|", end=" ")

            print(board[i][j], end=" ")

        print("|")
    print(25 * "-")


def main():
    # Initialise board
    board = []
    for i in range(9):
        row = 9 * [0]
        board.append(row)

    insert_number(1, board, 1, 3)
    print_board(board)


if __name__ == "__main__":
    main()