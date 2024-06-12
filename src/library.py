class Library:
    def __init__(self):
        self.objectList = []

    def addBook(self, book):
        self.objectList.append(book)

    def displayBooks(self):
        for object in self.objectList:
            print(object.displayAll())
    