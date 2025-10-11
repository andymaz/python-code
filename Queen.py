class EightQueen:
    """
    Solves the classic Eight Queens problem using backtracking.
    Ensures that no two queens threaten each other.
    """

    def __init__(self, board_size: int = 8):
        self.BOARD_SIZE = board_size
        self.board = [[0] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.count = 0  # number of solutions found

    # ───────────────────────────────────────────────────────────────
    # Utility methods
    # ───────────────────────────────────────────────────────────────

    def is_safe(self, row: int, column: int) -> bool:
        """
        Check if placing a queen at (row, column) is safe.
        No other queen should share the same column or diagonal.
        """
        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                if self.board[r][c] == 1:
                    # same column
                    if c == column:
                        return False
                    # diagonal (\)
                    if (r + c) == (row + column):
                        return False
                    # diagonal (/)
                    if (r - c) == (row - column):
                        return False
        return True

    def is_full(self) -> bool:
        """Return True if all queens have been placed."""
        count = sum(sum(row) for row in self.board)
        return count == self.BOARD_SIZE

    def safe_positions(self, row: int) -> list[int]:
        """
        Return a list of safe column indices for a queen in the given row.
        """
        return [c for c in range(self.BOARD_SIZE) if self.is_safe(row, c)]

    def print_solution(self):
        """
        Print the positions (columns) of the 8 queens.
        """
        self.count += 1
        print(f"{self.count}: ", end="")
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.board[row][column]:
                    print(f" {column + 1}", end="")
        print()

    # ───────────────────────────────────────────────────────────────
    # Recursive solver
    # ───────────────────────────────────────────────────────────────

    def solve(self, row: int = 0):
        """
        Recursive backtracking algorithm to place queens row by row.
        """
        if row >= self.BOARD_SIZE:
            return

        for column in self.safe_positions(row):
            self.board[row][column] = 1  # place queen
            self.solve(row + 1)

            if self.is_full():
                self.print_solution()

            # backtrack
            self.board[row][column] = 0


# ───────────────────────────────────────────────────────────────
# Main program
# ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    Q = EightQueen()
    Q.solve(0)
    print(f"\nTotal solutions found: {Q.count}")
