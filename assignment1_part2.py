
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def display(self):
        print("{title}, written by {author}".format(title=self.title, author=self.author))

b = ""
book = Book(b,b)
book1 = Book(title='Of Mice and Men', author='John Steinbeck')
book1.display()
book2 = Book(title='To Kill a Mockingbird', author='Harper Lee')
book2.display()
        
if __name__ == "__main__":
    pass
