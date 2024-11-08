import os
import sys
import django

# Step 1: Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Step 2: Set the environment variable to point to your project’s settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Initialize Django
django.setup()

#import the class from relationship_app
from relationship_app.models import Author, Book, Library, Librarian

#creating some author instances
author1 = Author(name= 'George Orwell')
author2= Author(name='Chinua Achebe')
author1.save()
author2.save()
#creating some books
book1 = Book(title='1984', author= author1)
book2 = Book(title='Things Fall Apart', author= author2)
book3= Book(title='Arrow of God', author = author2)
book1.save()
book2.save()
book3.save()

#query all books by a specific author// chinua achebe
all_books = author2.books.all()
for obj in all_books:
    print(obj)


#query to get the book id's 
id_books = author2.books.values_list('pk')

#Create a new Library Instance, and assigning books by author1
library1 = Library(name= 'Alx Library')
library1.save()
library1.books.add(book1.id)
library1.save()

#creating a Librarian who works at library1
librarian1 = Librarian(name='John Doe', library= library1)
librarian1.save()

#Listing all the books in the Library
print(library1.books.all())

#Retrieving the Librarian at Library One
print(library1.librarian)