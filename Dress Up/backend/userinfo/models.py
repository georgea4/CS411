from django.db import models
from .api import get_weather, get_news

# Create your models here.

list_display = ('id', 'user_email', 'location', 'weather', 'news','color')
class UserInfo(models.Model):
    id = models.CharField(max_length=320, default=0, primary_key=True)
    user_email = models.CharField(max_length=320, default="")
    location = models.TextField(default= "02215")
    weather = models.JSONField(default= {})
    news = models.JSONField(default= {})
    color = models.JSONField(default= {})

    def _str_(self):
        return self.title

    def save(self, *args, **kwargs):
        zip_string = self.location
        self.weather = get_weather(zip_string)
        self.news = get_news()
        super().save(*args, **kwargs) 
