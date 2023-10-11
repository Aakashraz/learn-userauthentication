from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Language(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title= models.CharField(max_length=100)
    author= models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary= models.TextField(max_length=600)
    isbn= models.CharField("ISBN", max_length=13, unique=True)
    genre= models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog:book_detail", kwargs={"pk": self.pk})
    
    
    

class Author(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    date_of_birth= models.DateField(null=True, blank=True)

    class Meta:
        ordering= ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

import uuid     #unique identifier generator

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book= models.ForeignKey(Book, on_delete=models.RESTRICT,null= True)
    imprint= models.CharField(max_length=100)
    due_back= models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('r', 'Reserved'),
        ('a', 'Available'),     
    )

    status= models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering= ['due_back']

    def __str__(self):
        return f'{self.id}, ({self.book.title})'