

class EightQueen(object):

    def __init__(self):
        self.BOARD_SIZE = 8
        self.board = [[0 for x in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        self.count = 0
        # self.safe_list = [0 for x in range(self.BOARD_SIZE)]

    def eight_queen(self):
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                self.board[row][column] = 0

    def check(self, row, column):
        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                if self.board[r][c] == 1 and c == column: # column
                    return 1
                if self.board[r][c] == 1 and (r + c) == (row + column): # diagonal \
                    return 1
                if self.board[r][c] == 1 and r - c == row - column: # diagonal /
                    return 1
        return 0

    def full(self):
        count = 0
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.board[row][column] == 1:
                    count += 1
        if count == self.BOARD_SIZE:
            return 1
        return 0

    def safe(self, row, lst):
        index = 0
        for column in range(self.BOARD_SIZE):
            if not self.check(row, column):
                lst[index] = column
                index += 1
        return index

    def print_solution(self):
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.board[row][column]:
                    print("   ", (column+1), end="")
        print()

    def queen(self, row):
        index = 0
        column = 0
        safe_list = [0 for x in range(self.BOARD_SIZE)]
        if row < self.BOARD_SIZE:
            index = self.safe(row,  safe_list)
        while column < index:
            self.board[row][safe_list[column]] = 1
            self.queen(row + 1)
            if self.full():
                self.print_solution()
            self.board[row][safe_list[column]] = 0
            column += 1

Q = EightQueen()
Q.queen(0)
