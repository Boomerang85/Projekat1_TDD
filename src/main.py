from book import Book
from library import Library

library = Library()

insert = input("\nDobrodošli u biblioteku. Šta biste želeli da uradite? \n\n1) Dodaj knjigu \n")

match insert:

    case "1":
        print("Koliko knjiga biste želeli da dodate?")
        
        n = int(input())
        
        i = 0

        while i < n:
            print ("Unesite naziv, autora, godinu izdanja i žanr knjige.\n")
            title = input("Naziv: ")
            author = input("Autor: ")
            releaseDate = input("Godina izdanja: ")
            genre = input("Žanr: ")
            book = Book(title, author, releaseDate, genre)
            library.addBook(book)
            print("Vaša knjiga je uspešno dodata u biblioteku.\n")
            i = i + 1

    case _:
        print("Molimo Vas odaberite validnu opciju.\n")
