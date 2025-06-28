from django.db import models

class ArticleView(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Добавили поле
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    imageUrl = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    publishedDate = models.CharField(max_length=100)
    sourceUrl = models.URLField(unique=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-viewed_at']

    def __str__(self):
        return f"{self.title} ({self.publishedDate})"
