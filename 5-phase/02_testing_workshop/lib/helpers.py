from os import get_terminal_size

term_size = get_terminal_size().columns


def term_wrap(string):
    star_line()
    center_string_stars(string)
    star_line()


def star_line():
    print("*" * term_size)


def center_string_stars(string):
    half_size = (term_size - len(string) - 2) / 2
    half_stars = "*" * int(half_size)
    print(f"{half_stars} {string} {half_stars}")
