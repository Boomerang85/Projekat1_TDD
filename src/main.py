from book import Book
from library import Library

library = Library()

insert = input("\nDobrodošli u biblioteku. Šta biste želeli da uradite? \n\n1) Dodaj knjigu \n2) Pretraži biblioteku\n")

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

        file = open("file.txt", "w")
        for object in library.objectList:
            file.write(object.displayAll() + "\n")
        file.close()

    case "2":
        searchCriteria = input("Navedite po čemu želite da tražite knjigu. Precizno napišite naslov, autor, godina izdavanja ili zanr\n")
        keyword = input("Navedite ključnu reč po kojoj želite da tražite knjigu\n")
        results = library.searchBooks(searchCriteria, keyword)
        print(results)

    case _:
        print("Molimo Vas odaberite validnu opciju.\n")
