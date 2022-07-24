from django.contrib import admin

from library.models import User,Book,Book_Ranted
# from mysite3.library.models import Book_Ranted

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Book_Ranted)

# Register your models here.
