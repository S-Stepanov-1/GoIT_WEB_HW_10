from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    fullname = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    born_date = models.DateField()
    born_location = models.CharField(max_length=250)
    photo = models.ImageField(default='default_image.png', upload_to='profile_images')

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.photo.path)


class Quote(models.Model):
    quote = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="quotes")
