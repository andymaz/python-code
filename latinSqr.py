class LatinSqrSolution:
    """
    Exhaustively generates all 3×3 magic squares using backtracking.
    Each row, column, and diagonal must sum to the same constant (15).
    """

    def __init__(self, size: int = 3):
        # Only designed for 3×3, but size is kept for flexibility
        self.size = size ** 2
        self.board = [0] * self.size

    def __str__(self) -> str:
        """Pretty-print the current 3×3 board."""
        out = ""
        for i in range(self.size):
            if i % 3 == 0:
                out += "\n"
            out += f"{self.board[i]:>3}"
        return out

    # ───────────────────────────────────────────────────────────────
    # Utility methods
    # ───────────────────────────────────────────────────────────────

    def to_be_placed(self):
        """Return a list of numbers not yet placed."""
        return [x for x in range(1, 10) if x not in self.board]

    def solved(self) -> bool:
        """Check whether the current board forms a 3×3 magic square."""
        b = self.board
        target = b[0] + b[1] + b[2]

        rows = [
            b[3] + b[4] + b[5],
            b[6] + b[7] + b[8],
        ]
        cols = [
            b[0] + b[3] + b[6],
            b[1] + b[4] + b[7],
            b[2] + b[5] + b[8],
        ]
        diags = [
            b[0] + b[4] + b[8],
            b[2] + b[4] + b[6],
        ]

        return all(s == target for s in rows + cols + diags)

    # ───────────────────────────────────────────────────────────────
    # Backtracking solver
    # ───────────────────────────────────────────────────────────────

    def latin_square(self, n: int = 0):
        """Recursive backtracking to generate magic squares."""
        if n < self.size:
            for x in self.to_be_placed():
                self.board[n] = x
                self.latin_square(n + 1)
                if n + 1 == self.size and self.solved():
                    print(self)
                self.board[n] = 0  # backtrack

# ───────────────────────────────────────────────────────────────
# Main entry point
# ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    s = LatinSqrSolution(3)
    s.latin_square(0)
