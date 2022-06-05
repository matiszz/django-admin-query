# Django Command to seed the database with test data
from django.core.management import BaseCommand

from example.models import Country, Author, Book, Category, Shop


class Command(BaseCommand):
    help = "Seeds the database with test data"

    def handle(self, *args, **options):

        Country.objects.create(name="USA", population=3000000)
        Country.objects.create(name="Canada", population=9000000)
        Country.objects.create(name="Mexico", population=2000000)
        Country.objects.create(name="Australia", population=2400000)
        Country.objects.create(name="New Zealand", population=4000000)
        Country.objects.create(name="France", population=6700000)
        Country.objects.create(name="Germany", population=8000000)
        Country.objects.create(name="Italy", population=6000000)

        Author.objects.create(
            name="J.R.R. Tolkien", country=Country.objects.get(name="USA"), age=54
        )
        Author.objects.create(
            name="Stephen King", country=Country.objects.get(name="USA"), age=50
        )
        Author.objects.create(
            name="George R.R. Martin", country=Country.objects.get(name="USA"), age=36
        )
        Author.objects.create(
            name="Margaret Atwood", country=Country.objects.get(name="Canada"), age=24
        )
        Author.objects.create(
            name="J.M. Barrie", country=Country.objects.get(name="Canada"), age=66
        )
        Author.objects.create(
            name="J.D. Salinger", country=Country.objects.get(name="Canada"), age=45
        )
        Author.objects.create(
            name="J.K. Rowling", country=Country.objects.get(name="France"), age=56
        )
        Author.objects.create(
            name="Estefano Rey", country=Country.objects.get(name="France"), age=71
        )

        a = Shop.objects.create(name="Amazon")
        b = Shop.objects.create(name="Ebay")
        g = Shop.objects.create(name="La tienda del libro")
        d = Shop.objects.create(name="Abacus")
        e = Shop.objects.create(name="El Corte Inglés")
        f = Shop.objects.create(name="La Illa")

        h = Category.objects.create(name="Fantasy")
        h.shops.set([a, b, g])
        i = Category.objects.create(name="Thriller")
        i.shops.set([a, b, d])
        j = Category.objects.create(name="History")
        j.shops.set([g, f, e])

        b = Book.objects.create(
            name="Harry Potter and the Philosopher's Stone",
            author=Author.objects.get(name="J.K. Rowling"),
            price=18.23,
            published_date="1997-07-01",
        )
        b.categories.set([h])
        b = Book.objects.create(
            name="Harry Potter and the Chamber of Secrets",
            author=Author.objects.get(name="J.K. Rowling"),
            price=16.68,
            published_date="1998-07-01",
        )
        b.categories.set([h, i])
        b = Book.objects.create(
            name="Harry Potter and the Prisoner of Azkaban",
            author=Author.objects.get(name="J.K. Rowling"),
            price=11.00,
            published_date="1999-07-01",
        )
        b.categories.set([h, i])
        b = Book.objects.create(
            name="Harry Potter and the Goblet of Fire",
            author=Author.objects.get(name="J.K. Rowling"),
            price=15.00,
            published_date="2000-07-01",
        )
        b.categories.set([h, i])
        b = Book.objects.create(
            name="Harry Potter and the Order of the Phoenix",
            author=Author.objects.get(name="J.K. Rowling"),
            price=14.10,
            published_date="2001-07-01",
        )
        b.categories.set([h, i])
        b = Book.objects.create(
            name="Harry Potter and the Half-Blood Prince",
            author=Author.objects.get(name="J.K. Rowling"),
            price=8.89,
            published_date="2002-07-01",
        )
        b.categories.set([h, i])
        b = Book.objects.create(
            name="Harry Potter and the Deathly Hallows",
            author=Author.objects.get(name="J.K. Rowling"),
            price=10.99,
            published_date="2003-07-01",
        )
        b.categories.set([h, i])
        b = Book.objects.create(
            name="The Hobbit",
            author=Author.objects.get(name="J.R.R. Tolkien"),
            price=19.99,
            published_date="1937-07-01",
        )
        b.categories.set([i, j])
        b = Book.objects.create(
            name="The Fellowship of the Ring",
            author=Author.objects.get(name="J.R.R. Tolkien"),
            price=9.99,
            published_date="1954-07-01",
        )
        b.categories.set([j])
