from django.db import models
import uuid
from django.utils import timezone

class Parsing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    published_date = models.CharField(max_length=100)
    source_url = models.URLField(unique=True)
    viewed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-viewed_at']

    def __str__(self):
        return f"{self.title} ({self.published_date})"
