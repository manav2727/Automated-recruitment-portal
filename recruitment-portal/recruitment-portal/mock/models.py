from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile

# Create your models here.
class MockIt(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='mockit', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content[:20])
    
    def snippet(self):
        return self.content[:100] + "..."

    class Meta:
        ordering = ('-created',)

class Mock(models.Model):
    title= models.TextField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title