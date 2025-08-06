#Create a Book class with attributes: title, author, and pages. Instantiate and print book details.
class Book:
    language = "English"
# Add a class variable language = "English" in the Book class. Access it from different instances
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
#Add method summary() to return a short description of the book
    def summary(self):
        return(f"'{self.title}, by {self.author} has {self.pages} pages.")
#Create a method is_lengthy() that returns True if pages > 300, else False.
    def is_lengthy(self):
        return self.pages >300
#Override _repr_() in the Book class to return a formatted book reference.
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
#Create an Author class with name and bio attributes, and a method introduce() that prints their intro
class Author:
    def __init__(self,name,bio):
        self.name = name
        self.bio = bio
    def introduce(self):
        print(f"Author: {self.name} \nBio: {self.bio}")
# Additional Challenges:
#Create a Library class with a list of books and a method to add new books.
class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
#Write a method in Library to count total pages of all books.
    def total_pages(self):
        return sum(book.pages for book in self.books)
book1 = Book("Python OOP", "Jhon Smith", 250)
book2 = Book("Advanced Python", "Alice Brown", 450)
#Add a method summary() to return a short description of the book.
print("Book 1 Summary:", book1.summary())
print("Book 2 Summary:", book2.summary())
#Create a method is_lengthy() that returns True if pages > 300, else False.
print("Is Book 1 lengthy?", book1.is_lengthy())
print("Is Book 2 lengthy?", book2.is_lengthy())
#Add a class variable language = "English" in the Book class. Access it from different instances.
print("\nAccessing class variable")
print("Access via class:", Book.language)
print("Access via book1:", book1.language)
print("Access via book2:", book2.language)
#Create two Book instances and check if they are equal using == and explain the output.
print("\nAre book1 and book2 equal?", book1 == book2)
# Create an Author class with name and bio attributes, and a method introduce() that prints their intro.
author = Author("Alice Brown", "Expert in Python programming.")
author.introduce()
#Create a Library class with a list of books and a method to add new books.
library = Library()
library.add_book(book1)
library.add_book(book2)
#Write a method in Library to count total pages of all books.
print("\nTotal pages in library:", library.total_pages())
#Override _repr_() in the Book class to return a formatted book reference.
print("Book representation (repr):", repr(book1))
#Use the type() and id() functions on an object and explain what they return.
print("\nType of book1:", type(book1))
print("ID of book1 object:", id(book1))