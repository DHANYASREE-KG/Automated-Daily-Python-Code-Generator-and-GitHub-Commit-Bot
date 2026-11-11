"""
Tower of Hanoi Solver.

Classic recursion problem moving n disks from source peg to target peg using an auxiliary peg.
"""


def solve_hanoi(n: int, source: str, target: str, auxiliary: str) -> list[str]:
    """Generate sequence of disk movements to solve Tower of Hanoi."""
    moves = []

    def _hanoi(disks, src, tgt, aux):
        if disks == 1:
            moves.append(f"Move disk 1 from {src} to {tgt}")
            return
        _hanoi(disks - 1, src, aux, tgt)
        moves.append(f"Move disk {disks} from {src} to {tgt}")
        _hanoi(disks - 1, aux, tgt, src)

    _hanoi(n, source, target, auxiliary)
    return moves


if __name__ == "__main__":
    print("=== Tower of Hanoi (3 Disks) ===")
    steps = solve_hanoi(3, "A", "C", "B")
    for step in steps:
        print(step)
