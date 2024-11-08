from django.db import models

class Book(models.Model):
    """
    Represents a book in the library.

    This model maps to a table called 'Books' in the database 'New_Library'.
    The table will have three attributes:
        - title: A string representing the book's title (max length: 200).
        - author: A string representing the book's author (max length: 100).
        - publication_year: An integer representing the year the book was published.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"'{self.title}' by {self.author}. Publication Year: {self.publication_year}"
    
    def __repr__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.publication_year}'
