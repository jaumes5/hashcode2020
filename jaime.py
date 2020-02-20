def parser(path):
    with open(path, 'r') as file:
        data = file.read()
    data = data.split('\n')
    B, L, D = [int(i)for i in data[0].split(' ')]
    books_score = data[1].split()
    library = []
    for i in range(L):
        N, T, M = [int(i)for i in data[2+i*2].split()]
        books = [int(i)for i in data[3+i*2].split()]
        library.append({'number_B':N, 'number_D':T, 'number_S': M, 'books': books})
    return B, L, D, books_score, library



