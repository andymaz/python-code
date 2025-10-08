class MagicSquare:
    """
    Generate and verify n×n magic squares using backtracking.
    A magic square has all rows, columns, and diagonals summing to the same value.
    """

    def __init__(self, n: int):
        self.n = n
        self.size = n * n
        self.board = [0] * self.size

    def __str__(self):
        """Return a formatted string representation of the board."""
        output = ""
        for i, val in enumerate(self.board):
            if i % self.n == 0:
                output += "\n"
            output += f"{val:4}"
        return output

    def solved(self) -> bool:
        """Check if the current board satisfies the magic square condition."""
        b = self.board
        n = self.n

        # Compute all row sums
        rows = [sum(b[i * n:(i + 1) * n]) for i in range(n)]
        # Compute all column sums
        cols = [sum(b[i::n]) for i in range(n)]
        # Compute diagonals
        diag1 = sum(b[i * (n + 1)] for i in range(n))
        diag2 = sum(b[(i + 1) * (n - 1)] for i in range(n))

        # Check if all sums are equal
        all_sums = rows + cols + [diag1, diag2]
        return len(set(all_sums)) == 1

    def to_be_placed(self):
        """Return numbers that have not yet been placed on the board."""
        return [x for x in range(1, self.size + 1) if x not in self.board]

    def generate(self, pos: int = 0):
        """
        Recursively fill the grid with numbers and print
        configurations that form valid magic squares.
        """
        if pos < self.size:
            for x in self.to_be_placed():
                self.board[pos] = x
                self.generate(pos + 1)
                # When full board is filled, check if it's a magic square
                if pos + 1 == self.size and self.solved():
                    print(self)
                self.board[pos] = 0  # Backtrack


if __name__ == "__main__":
    n = 3  # You can change this to 4, 5, etc.
    ms = MagicSquare(n)
    ms.generate(0)
