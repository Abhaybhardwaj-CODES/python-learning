class Library:
    def __init__(self,book,author,year):
        self.book = book
        self.author = author
        self.year = year

    def display(self):
        print("Book:", self.book)
        print("Author:", self.author)
        print("Year:", self.year)