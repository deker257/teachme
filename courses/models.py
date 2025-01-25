from django.db import models
from users.models import Users
from category.models import Category

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    rate = models.FloatField(default=0, blank=True)
    released = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='courses/thumbnails/', blank=True)
    video = models.FileField(upload_to='courses/videos/', blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    # video_url = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.title
