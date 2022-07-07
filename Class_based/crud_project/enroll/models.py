from django.db import models

from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    Reg_no=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    Semester=models.IntegerField()
     
    def __str__(self):
        return self.name,

    
    # Password=models.CharField(max_length=70)



# Create your models here.
