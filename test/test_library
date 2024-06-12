from io import StringIO

import unittest

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from book import Book
from library import Library

class Test_Libary(unittest.TestCase):
    def test_includeBook(self):
        book = Book(title = any, author = any, releaseDate = any, genre = any)
        library = Library()
        library.addBook(book)
        self.assertEqual(len(library.objectList), 1)

    def test_displayBooks(self):
        book = Book(title = any, author = any, releaseDate = any, genre = any)
        library = Library()
        capture_output = StringIO()
        sys.stdout = capture_output
        library.displayBooks()
        sys.stdout = sys.__stdout__
        if capture_output.getvalue().strip() == book:
            return True


if __name__ == '__main__':
   unittest.main()