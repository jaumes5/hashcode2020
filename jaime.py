import math


def parser(path):
    with open(path, "r") as file:
        data = file.read()
    data = data.split("\n")
    B, L, D = [int(i) for i in data[0].split(" ")]
    books_score = data[1].split()
    library = []
    for i in range(L):
        N, T, M = [int(i) for i in data[2 + i * 2].split()]
        books = [int(i) for i in data[3 + i * 2].split()]
        days = math.ceil(N / M)
        books_score_d = sum(books_score[i] for i in books) / days
        library.append(
            {
                "number_B": N,
                "number_D": T,
                "number_S": M,
                "books": books,
                "score_d": books_score_d,
                "days": days,
                "score": 0,
            }
        )
    return B, L, D, books_score, library
