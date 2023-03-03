from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile

class Domains(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='domain', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='domain')

    def __str__(self):
        return str(self.content[:20])
    
    def snippet(self):
        return self.content[:100] + "..."

    class Meta:
        ordering = ('-created',)

class Sde(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='sde', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sde')

    def __str__(self):
        return str(self.content[:20])
    
    def snippet(self):
        return self.content[:100] + "..."

    class Meta:
        ordering = ('-created',)

class Finance(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='finance', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='finance')

    def __str__(self):
        return str(self.content[:20])
    
    def snippet(self):
        return self.content[:100] + "..."

    class Meta:
        ordering = ('-created',)



