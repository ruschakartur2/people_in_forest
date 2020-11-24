from django.db import models


class Seed(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Image(models.Model):
    image_link = models.CharField(max_length=500)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Panorama(models.Model):
    title = models.CharField(max_length=100)
    images = models.ManyToManyField(Image)
    panorama_url = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Marker(models.Model):
    street = models.CharField(max_length=100)
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
    panorama = models.ForeignKey(Panorama, on_delete=models.CASCADE)

    def __str__(self):
        return self.street


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    facebook_link = models.CharField(max_length=500)
    is_administration = models.BooleanField()

    def __str__(self):
        return self.name
