symbol = 4
In_the_line = 4 * 25
On_the_page = 50 * In_the_line
In_book = 100 * On_the_page
in_byte = 1.44 * 1024 * 1024
books = in_byte / In_book
answer = round(books)
print('Количество книг, помещающихся на дискету:', answer)