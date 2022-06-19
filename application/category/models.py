from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)
    imgpath = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Branch(models.Model):
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.address


class Contact(models.Model):

    class Type(models.IntegerChoices):
        PHONE = 1,
        FACEBOOK = 2,
        EMAIL = 3

    type = models.IntegerField(choices=Type.choices)
    value = models.CharField(max_length=250)

    def __str__(self):
        return self.value


class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    logo = models.CharField(max_length=20, blank=True)
    contacts = models.ManyToManyField(Contact)
    branches = models.ManyToManyField(Branch, blank=True)

    def __str__(self):
        return self.name

