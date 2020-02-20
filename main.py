from jaime import *
from gauthier import *

if __name__ == "__main__":
    B, L, D, books_score, library = parser("files/a_example.txt")
    #generate_output(library, books_score, D)
    score = score('files/output.txt', books_score)
    print(score)
    pass
