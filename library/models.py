from django.db import models

# Create your models here.
from django.db import models

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    available_copies = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"

# Member model
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_date = models.DateField()

    def __str__(self):
        return self.name

# BorrowRecord model
class BorrowRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.member} borrowed {self.book}"
