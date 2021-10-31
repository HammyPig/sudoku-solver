from slot import Slot

class Board:

    BOARD_SIZE = 9
    SQUARE_SIZE = 3

    def __init__(self, path=None):
        self.rows = []

        if not path:
            for i in range(Board.BOARD_SIZE):
                row = Board.BOARD_SIZE * [Slot(0)]
                self.rows.append(row)
        else:
            self.rows = self.read_board(path)


    def __str__(self):
        string = ""

        i = 0
        for i in range(Board.BOARD_SIZE):
            # print horizontal separator every 3 rows
            if i % Board.SQUARE_SIZE == 0:
                string += 25 * "-" + "\n" 

            for j in range(Board.BOARD_SIZE):
                # print vertical separator every 3 columns
                if j % Board.SQUARE_SIZE == 0:
                    string += "| "
                string += str(self.rows[i][j]) + " "

            string += "|\n"
        string += 25 * "-"

        return string

    
    def read_board(self, path):
        with open(path, "r") as f:
            board = []
            for i in range(9):
                row = f.readline()
                row = row.rstrip("\n")
                row = list(row)

                for i in range(len(row)):
                    value = int(row[i])
                    row[i] = Slot(value)
                board.append(row)
        
        return board
    

    def insert_number(self, value, row, col):
        row -= 1
        col -= 1
        self.rows[row][col] = value

    
    def print_possible_values(self):
        for i in range(Board.BOARD_SIZE):
            # print horizontal separator every 3 rows
            if i % Board.SQUARE_SIZE == 0:
                print(97 * "-")

            for j in range(Board.BOARD_SIZE):
                # print vertical separator every 3 columns
                if j % Board.SQUARE_SIZE == 0:
                    print("|", end=" ")

                self.rows[i][j].print_possible_values()
                
            print("|")
        print(97 * "-")
