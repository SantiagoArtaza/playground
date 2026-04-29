from symtable import Class

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Author(models.Model):
    name = models.CharField(max_length=100) 
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name= models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    published_date=models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books') # related_name allows us to access the books of an author using author.books.all
    pages = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=20, unique=True)
    genres=models.ManyToManyField(Genre,related_name='books') #related name permite acceder a libros desde generos
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField(null=True, blank=True)
    createated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.reviewer.username} - {self.book.title} ({self.rating}/5)"
    
    
#book1 = Book.objects.create(title="1984", published_date="1949-06-08", author= orwell,pages=300 ,isbn="123455656")