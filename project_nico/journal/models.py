from django.conf import settings
from django.db import models

# Create your models here.

# Journal entry model
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=70)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title