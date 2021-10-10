searching_book = input()
book_count = 0

while True:
    current_book = input()
    if current_book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {book_count} books.')
        break

    if current_book == searching_book:
        print(f'You checked {book_count} books and found it.')
        break

    book_count += 1







  
 
  
  
  
