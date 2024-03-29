from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.category_name
    
class AuthorBook(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='author_book', default='static/authimg/authimg.png', blank=True)
    desctiption = models.TextField()
    gender = models.BooleanField(default=True, blank=True, help_text='Is author\'s gender male')

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    author_book = models.ForeignKey(AuthorBook, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=200)
    pags = models.PositiveIntegerField()
    isbn = models.PositiveIntegerField()
    text_format = models.CharField(max_length=40)
    synopsis = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.book_name
    
class Advertisement(models.Model):
    img = models.ImageField(upload_to='advertisement')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.product.book_name
