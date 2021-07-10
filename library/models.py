from django.db import models


class Author(models.Model):  
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    title = models.TextField(max_length=50)


    def __str__(self):
        return self.title


class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=0)  
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.CASCADE, related_name="books")
    image = models.ImageField(upload_to='covers', null=True, blank=True)


    def __str__(self):
        return self.title


class Friend(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)

    def __str__(self):
        res = "{} {}".format(self.first_name, self.last_name)
        return res


class Friend(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)

    def __str__(self):
        res = "{} {}".format(self.first_name, self.last_name)
        return res

class FriendBook(models.Model):
    friend_name = models.ForeignKey(Friend, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_in = models.DateTimeField()
    date_out = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        res = "{} - {}".format(self.friend_name, self.book)
        return res