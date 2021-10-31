from slot import Slot

class Board:

    BOARD_SIZE = 9
    SQUARE_SIZE = 3

    def __init__(self, path=None):
        self.unknown_values = []
        self.rows = []

        if not path:
            for i in range(Board.BOARD_SIZE):
                row = []
                for j in range(Board.BOARD_SIZE):
                    slot = Slot(i, j, 0)
                    row.append(slot)
                    self.unknown_values.append(slot)
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

                for j in range(len(row)):
                    value = int(row[j])
                    slot = Slot(i, j, value)
                    row[j] = slot

                    if value == 0:
                        self.unknown_values.append(slot)

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
    

    def get_slot_row(self, row, col):
        return self.rows[row]

    
    def get_slot_col(self, row, col):
        column = []
        for i in range(Board.BOARD_SIZE):
            column.append(self.rows[i][col])

        return column

    
    def get_slot_square(self, row, col):
        # round down to interval of 3
        row_square = row // 3 * 3
        col_square = col // 3 * 3

        square = []
        for row in self.rows[row_square:row_square + 3]:
            square += row[col_square:col_square + 3]

        return square


    def trim_possible_slot_values(self, row, col):
        value_found = False

        impossible_values = []
        row_values = self.get_slot_row(row, col)
        col_values = self.get_slot_col(row, col)
        square_values = self.get_slot_square(row, col)

        impossible_values = row_values + col_values + square_values
        impossible_values = set(impossible_values)

        for n in impossible_values:
            self.rows[row][col].remove_possible_value(n)
        
        if len(self.rows[row][col].possible_values) == 1:
            self.rows[row][col].value = self.rows[row][col].possible_values[0]
            value_found = True
        
        return value_found

    
    def trim_possible_values(self):
        new_value_found = False
        for slot in self.unknown_values:
            if self.trim_possible_slot_values(slot.row, slot.col):
                self.unknown_values.remove(slot)
                new_value_found = True
        
        return new_value_found


    def solve(self):
        # loop until nothing further can be found
        while self.trim_possible_values():
            pass
        
        if not self.unknown_values:
            return True
        else:
            return False
