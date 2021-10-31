from board import Board


def main():
    board = Board("puzzles/easy-1.txt")
    print(board)
    board.print_possible_values()
    board.trim_possible_values()
    board.print_possible_values()
    print(board)


if __name__ == "__main__":
    main()
