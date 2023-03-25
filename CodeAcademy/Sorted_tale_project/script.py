import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
for book in bookshelf:
    print(book['title'])

print (ord("a"))
print(ord(" "))
print(ord("A"))
# when sorting, we do not want to take account the case of the letters. For example, “cats” should come before “Dogs”, even though ord("c") > ord("D") is True.

book['author_lower'] = book['author'].lower()