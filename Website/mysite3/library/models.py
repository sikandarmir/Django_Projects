from pyexpat import model
from django.db import models

from unicodedata import name
from django.db import models

# Create your models here.
class User(models.Model):
    User_name=models.CharField(max_length=70)
    # Reg_no=models.CharField(max_length=70)
    Email=models.EmailField(max_length=70)
    # Password=models.CharField()
    Password=models.CharField(max_length=50)
    # password=model.


    # def __str__(self):
    #     return self.User_name,

    
    # Password=models.CharField(max_length=70)



class Book(models.Model):
    Book_id = models.IntegerField(primary_key = True)
    Book_Name = models.CharField(max_length=50)
    Book_description = models.CharField(max_length=100)
    price = models.IntegerField()
    num_books = models.IntegerField()
    # book_type = models.TextChoices('Poetry','Physics')
    Book_types = models.CharField(max_length=10)
#One To Many Relationship

class Book_Ranted(models.Model):
    Book_ranted_id = models.IntegerField(primary_key = True)
    Book_foreign_id = models.author = models.ForeignKey(Book, on_delete=models.CASCADE)
    num_ranted_books = models.IntegerField()

    # address = models.CharField(max_length=150)
