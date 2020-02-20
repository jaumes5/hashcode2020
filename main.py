from jaime import *


if __name__ == "__main__":
    B, L, D, books_score, library = parser("files/f_libraries_of_the_world.txt")
    generate_output(library, books_score, D)
    pass
