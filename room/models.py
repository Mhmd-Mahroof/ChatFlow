from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    desc=models.TextField(null=True)
    img=models.ImageField(upload_to='room_images',null=True)

    def __str__(self):
        return self.name

class Messages(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE,related_name='messages')
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='messages')
    content=models.TextField()
    date_added=models.DateTimeField( auto_now_add=True)

    class Meta:
        ordering=('date_added',)