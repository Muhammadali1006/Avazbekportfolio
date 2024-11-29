from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=221)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    description = models.TextField()
    image = models.ImageField(upload_to="image_project/")
    url = models.URLField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=110)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Human(models.Model):
    name = models.CharField(max_length=221)
    description = models.TextField()
    image = models.ImageField(upload_to="human_image/")
    job = models.CharField(max_length=221)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Sumary(models.Model):
    description = models.TextField()
    city = models.CharField(max_length=110)
    number = models.CharField(max_length=110)
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city

class Education(models.Model):
    name = models.CharField(max_length=110)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProfessionalExperience(models.Model):
    pro_name = models.CharField(max_length=110)
    name = models.CharField(max_length=110)
    one_description = models.TextField()
    two_description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pro_name


class Servise(models.Model):
    name = models.CharField(max_length=110)
    description = models.TextField()
    image = models.ImageField(upload_to="servise_image/")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name