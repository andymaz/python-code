class Latin:
    """
    Generate and check 3×3 Latin-like squares where all rows, columns,
    and diagonals sum to the same value (a "magic square"-style constraint).
    """

    def __init__(self, size: int):
        self.size = size ** 2
        self.board = [0] * self.size  # Flattened 3×3 grid as a list

    def __str__(self):
        """Return a formatted string representation of the board."""
        output = ""
        for i, val in enumerate(self.board):
            if i % 3 == 0:
                output += "\n"
            output += f"  {val}"
        return output

    def solved(self) -> bool:
        """
        Check whether the current 3×3 board satisfies the magic square condition:
        all rows, columns, and both diagonals have equal sums.
        """
        b = self.board
        target = b[0] + b[1] + b[2]
        return (
            b[3] + b[4] + b[5] == target and
            b[6] + b[7] + b[8] == target and
            b[0] + b[3] + b[6] == target and
            b[1] + b[4] + b[7] == target and
            b[2] + b[5] + b[8] == target and
            b[0] + b[4] + b[8] == target and
            b[2] + b[4] + b[6] == target
        )

    def to_be_placed(self):
        """Return a list of numbers (1–9) not yet placed on the board."""
        return [x for x in range(1, 10) if x not in self.board]

    def latin_square(self, n: int):
        """
        Recursively fill the 3×3 grid with numbers 1–9 and print
        each configuration that satisfies the 'solved' condition.
        """
        if n < self.size:
            for x in self.to_be_placed():
                self.board[n] = x
                self.latin_square(n + 1)
                # When full board is filled, check if solved
                if n + 1 == self.size and self.solved():
                    print(self)
                self.board[n] = 0  # Backtrack


if __name__ == "__main__":
    latin = Latin(3)
    latin.latin_square(0)
