class Library:
    def __init__(self):
        self.objectList = []

    def addBook(self, book):
        self.objectList.append(book)

    def displayBooks(self):
        for object in self.objectList:
            print(object.displayAll())

    def searchBooks(self, searchCriteria, keyword):
        results = []
        file = open("file.txt", "r")

        for line in file:
            bookData = line.strip().split(", ")

            match searchCriteria.lower():

                case "naslov":
                    if keyword.lower() in bookData[0].lower():
                        results.append(bookData)

                case "autor":
                    if keyword.lower() in bookData[1].lower():
                        results.append(bookData)

                case "godina izdavanja":
                    if keyword.lower() in bookData[2].lower():
                        results.append(bookData)

                case "zanr":
                    if keyword.lower() in bookData[3].lower():
                        results.append(bookData)

                case _:
                    return "Uneta reč nije validna."
            return results