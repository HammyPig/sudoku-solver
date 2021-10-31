from board import Board


def main():
    board = Board("puzzles/easy-1.txt")
    print(board)
    board.print_possible_values()
    print(board.get_slot_row(9, 2))
    print(board.get_slot_col(9, 2))
    print(board.get_slot_square(9, 2))


if __name__ == "__main__":
    main()