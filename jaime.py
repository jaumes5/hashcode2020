import math


def parser(path):
    with open(path, "r") as file:
        data = file.read()
    data = data.split("\n")
    B, L, D = [int(i) for i in data[0].split(" ")]
    books_score = [int(i) for i in data[1].split(" ")]
    library = {}
    for i in range(L):
        N, T, M = [int(i) for i in data[2 + i * 2].split()]
        books = [int(i) for i in data[3 + i * 2].split()]
        days = math.ceil(N / M)
        books_score_d = sum(books_score[i] for i in books) / days
        books = sorted(books, key=lambda a: books_score[a], reverse=True)
        days = min(D, days + T)
        score = (sum(books_score[i] for i in books[:(days-T)*M]) / days) * (D/T)
        library[i] = {
            "number_B": N,
            "number_D": T,
            "number_S": M,
            "books": books,
            "score_d": books_score_d,
            "days": days,
            "score": score,
        }
    return B, L, D, books_score, library

def reset_score(days_r, library, books_score):
    for i in library.keys():
        days = math.ceil(library[i]['number_B'] / library[i]['number_S'])
        days = min(days_r, days + library[i]['number_D'])
        score = sum(books_score[j] for j in library[i]['books'][:days * library[i]["number_S"]]) / days
        library[i]['score'] = score
    return library



def generate_output(library, books_score, D, path):
    resul = sorted(library.items(), key=lambda a: a[1]["score"], reverse=True)
    d = 0
    stage = []
    num_li = 0
    lista = []
    old = 1
    for i in resul:
        # d += i[1]["number_D"]
        if d == D:
            break
        if d + i[1]["number_D"] < D:
            d += i[1]["number_D"]
            num_li += 1
            tmp_d = D - d
            tmp_d = min(i[1]["days"], tmp_d)
            books = [str(i) for i in i[1]["books"][: tmp_d * i[1]["number_S"]]]
            lista.append(((str(i[0]), str(len(books))), books))
            ele_rem = i[0]
    with open(path, "w") as file:
        file.write(str(num_li) + "\n")
        for i in lista:
            file.write(" ".join(i[0]) + "\n")
            file.write(" ".join(i[1]) + "\n")
