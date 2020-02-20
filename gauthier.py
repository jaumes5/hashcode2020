def score(libraries, books_score):
    with open(libraries, "r") as file:
        data = file.read()
    data = data.split("\n")
    A = int(data[0])
    score = 0
    scanned_books = set()
    for i in range(A):
        Y, K = [int(i) for i in data[1+2*i].split(" ")]
        books = [int(i) for i in data[2*(i+1)].split(" ")]
        # print(scanned_books)
        for book in books:
            if book not in scanned_books:
                score += books_score[book]
                scanned_books.add(book)
    return score
