from board import Board


def main():
    puzzles = ["easy-1",
               "easy-2",
               "easy-3",
               "easy-4",
               "easy-5",
               "medium-1",
               "medium-2",
               "medium-3",
               "medium-4",
               "medium-5",
               "hard-1",
               "hard-2",
               "hard-3",
               "hard-4",
               "hard-5",
               "extra-hard-1",
               "extra-hard-2",
               "extra-hard-3",
               "extra-hard-4",
               "extra-hard-5"
               ]
    
    for puzzle in puzzles:
        print("solving", puzzle, "...")
        board = Board("puzzles/" + puzzle + ".txt")
        print(board)
        if not board.solve():
            print(board)
            board.print_possible_values()
            raise AssertionError
        print(board)


if __name__ == "__main__":
    main()
