```python
#Importing the Book model from the bookshelf app
>>> from bookshelf.models import Book

#Checking all books in the database
>>> Book.objects.all()
    # Expected Output: <QuerySet [Title: Nineteen Eighty-Four, Author: George Orwell, Year: 1949]>

#Delete the book
>>> Book.objects.all().delete()
    # Expected Output: (1, {'bookshelf.Book': 1})

# Confirm deletion by retrieving all Book objects
>>> Book.objects.all()
    # Expected Output: <QuerySet []>


