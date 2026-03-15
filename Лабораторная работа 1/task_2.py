# TODO Найдите количество книг, которое можно разместить на дискете
disc_size = 1.44 * 1024 * 1024
book_symb = 100 * 50 * 25
symb_size = 4
book_byte = book_symb * symb_size
book_number = disc_size // book_byte
print("Количество книг, помещающихся на дискету:", int(book_number))
