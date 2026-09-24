# Print recipe list
default:
    @just --list --unsorted

# Run the 4-bit adder program
run:
    uv run pi-4-bit-adder

format:
    ruff check --fix
