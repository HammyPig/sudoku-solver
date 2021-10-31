from board import Board


def main():
    board = Board("puzzles/easy-1.txt")
    print(board)
    board.print_possible_values()
    board.trim_possible_slot_values(1, 1)
    board.print_possible_values()


if __name__ == "__main__":
    main()