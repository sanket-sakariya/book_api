from django.db import models
from datetime import date

def cover_upload_path(instance, filename):
    return f"covers/{filename}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to=cover_upload_path, null=True, blank=True)

    def __str__(self):
        return self.title
