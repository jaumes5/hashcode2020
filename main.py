from jaime import *
from gauthier import *

if __name__ == "__main__":
    path = ("a_example.txt",
            "b_read_on.txt",
            "c_incunabula.txt",
            "d_tough_choices.txt",
            "e_so_many_books.txt",
            "f_libraries_of_the_world.txt")
    for i in path:
        B, L, D, books_score, library = parser("files/" + i)
        output = "files/output" + i[:-4] + ".txt"
        generate_output(library, books_score, D, output)
        scor = score(output, books_score)
        print(scor)
    pass
