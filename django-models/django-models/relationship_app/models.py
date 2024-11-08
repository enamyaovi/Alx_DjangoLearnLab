from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Represents an author of a book 
    
    It models a table with similar name in database 'NewLibrary'
        The model will have one attribute
    """

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    """
    Represents a book in the Library
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"
    

class Library(models.Model):
    """
    Represents a library with books
    """
    name = models.CharField(max_length=200)
    books = models.ManyToManyField (Book, related_name='library')

    def __str__(self) -> str:
        return self.name
    

class Librarian(models.Model):
    """
    Represents a Librarian who works at a Library
    """
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
