from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    categories = models.ManyToManyField("Category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    shops = models.ManyToManyField("Shop")

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
