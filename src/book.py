class Book:
    def __init__(self, title, author, releaseDate, genre):
        self.title = title
        self.author = author
        self.releaseDate = releaseDate
        self.genre = genre
        
    def displayAll(self):
        return f'{self.title}, {self.author}, {self.releaseDate}, {self.genre}'