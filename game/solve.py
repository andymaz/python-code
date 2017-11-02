from board import Puzzle


class Solve(object):
    def __init__(self, b, out):
        self.board = b
        self.puzzle = b.puzzle
        self.file = out

    # for any row i, this function returns all elements
    # that are not in that row
    def row(self, i):
        s = []
        for j in range(9):
            if not (self.puzzle[i][j] == 0):
                s.append(self.puzzle[i][j])
        return s

    # for any column j, this function returns all elements
    # that are not in that column
    def column(self, j):
        s = []
        for i in range(9):
            if not (self.puzzle[i][j] == 0):
                s.append(self.puzzle[i][j])
        return s

    # for any cell (i, j) this function returns all elements
    # that are not in the same box
    def box(self, i, j):
        si = self.find_box_start(i)
        sj = self.find_box_start(j)
        s = []
        for p in range(si, si + 3):
            for q in range(sj, sj + 3):
                if not (self.puzzle[p][q] == 0):
                    s.append(self.puzzle[p][q])
        return s

    # for any given x or y it calculates the starting point
    # of the box they belong to
    @staticmethod
    def find_box_start(n):
        return 3 * (n//3)

    # for any cell (i, j) this function all potential possible
    # entries given the configuration of the board
    def possibilities(self, i, j):
        s = []
        if self.puzzle[i][j] == 0:
            s.extend(self.row(i))
            s.extend(self.column(j))
            s.extend(self.box(i, j))
            return [p for p in range(1, 10) if p not in s]

    def is_unique(self, r, c):
        if not self.row_unique(r, c):
            return False
        if not self.column_unique(r, c):
            return False
        return self.box_unique(r, c)

    def row_unique(self, r, c):
        e = self.puzzle[r][c]
        for j in range(9):
            if j != c and self.puzzle[r][j] == e:
                return False
        return True

    def column_unique(self, r, c):
        e = self.puzzle[r][c]
        for i in range(9):
            if i != r and self.puzzle[i][c] == e:
                return False
        return True

    def box_unique(self, r, c):
        si = self.find_box_start(r)
        sj = self.find_box_start(c)
        e = self.puzzle[r][c]
        for p in range(si, si + 3):
            for q in range(sj, sj + 3):
                if p != r and q != c and self.puzzle[p][q] == e:
                    return False
        return True

    def solved(self):
        for i in range(9):
            for j in range(9):
                r = self.is_unique(i, j)
                if not r:
                    return False
        return True

    def to_file(self):
        for i in range(9):
            for j in range(9):
                self.file.write(str(self.puzzle[i][j]) + ' ')
                if j % 3 == 2:
                    self.file.write('\t')
            self.file.write('\n')
            if i % 3 == 2:
                self.file.write('\n')

    def sudoku(self, n):
        if n < 81:
            r, c = Puzzle.index(n)
            # print(self.puzzle[r][c])
            if self.puzzle[r][c] == 0:
                ps = self.possibilities(r, c)
                for x in ps:
                    self.puzzle[r][c] = x  # tentative placing of value x at position n
                    self.sudoku(n + 1)
                    # checking if the game is full and a solution is found
                    if n+1 == 81: # and self.solved():
                        print(self.board)
                        self.to_file()
                    self.puzzle[r][c] = 0  # backtracking
            else:
                # checking if the game is full and a solution is found
                if n+1 == 81: # and self.solved():
                    print(self.board)
                    self.to_file()
                self.sudoku(n + 1)
