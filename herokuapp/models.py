from django.contrib.auth import get_user_model
from django.db import models
from django.http import request

User = get_user_model()
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100,unique=True)
    movie_img = models.ImageField(upload_to='images/', default='images/default.png') 
    youtube_url = models.URLField(default='https://www.youtube.com/watch?v=6Jg_rkKtJgo')
    description = models.TextField()
    category = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
     