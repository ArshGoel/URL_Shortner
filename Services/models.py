from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Url(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    target_url = models.URLField()
    alias = models.CharField(max_length = 20,unique = True)
    timestamp = models.DateTimeField(auto_now_add= True)
    clicks = models.IntegerField(default=0)
    clicks_per_day = models.IntegerField(default=0)
    clicks_per_month = models.IntegerField(default=0)

    class Meta:
        ordering = ("-timestamp",)