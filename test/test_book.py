import unittest

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from book import Book

class Test_Book(unittest.TestCase):
    def test_createBook(self):
       Book(title = any, author = any, releaseDate = any, genre = any)

    def test_titleAdd(self):
      book = Book(title = "naslov", author = any, releaseDate = any, genre = any)
      if book == book.title:
         return True

    def test_authorAdd(self):
      book = Book(title = "naslov", author = "autor", releaseDate = any, genre = any)
      if book == book.author:
         return True

    def test_releaseDateAdd(self):
       book = Book(title = "naslov", author = "autor", releaseDate = "godina izdavanja", genre = any)
       if book == book.releaseDate:
         return True
    
    def test_genreAdd(self):
       book = Book(title = "naslov", author = "autor", releaseDate = "godina izdavanja", genre = "zanr")
       if book == book.genre:
         return True

    def test_displayAll(self):
       book = Book(title = "naslov", author = "autor", releaseDate = "godina izdavanja", genre = "zanr")
       if book == book.displayAll:
        return True
    

if __name__ == '__main__':
   unittest.main()