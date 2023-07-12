from os import get_terminal_size

def term_wrap(string):
    term_size = get_terminal_size().columns
    half_size = (term_size - len(string) - 2) / 2
    half_stars = "*" * int(half_size)
    print("*" * term_size)
    print(f"{half_stars} {string} {half_stars}")
    print("*" * term_size)
