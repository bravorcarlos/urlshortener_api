from django.db import models
from hashids import Hashids

# Create your models here.
class Link(models.Model):
    url = models.URLField(max_length=200)
    code = models.TextField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    click_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.code:
            self.code = Hashids(min_length=8).encode(self.pk)
            self.save()
