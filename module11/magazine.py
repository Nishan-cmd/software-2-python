class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages_count):
        self.name = name
        self.author = author
        self.pages_count = pages_count

    def print_info(self):
        print(self.name)
        print(self.author)
        print(self.pages_count)

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_info(self):
        print(self.name)
        print(self.chief_editor)

magazine = Magazine( name = "Muna Madan", chief_editor = "Laxmi Prasad")
book = Book("Python", author = "Happy", pages_count = 345)

magazine.print_info()
print()
book.print_info()