import uuid
from django.db import models
from django.conf import settings

# Class to get data after process algorithm and save to database
class PlagiarismCheck(models.Model):
    received_id = models.IntegerField(null=True)
    sentence1 = models.TextField(blank=True, null=True)
    sentence2 = models.TextField(blank=True, null=True)
    err_msg = models.TextField()
    is_paraphrase = models.BooleanField(default=False)
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)
    method = models.CharField(max_length=20)



