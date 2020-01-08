import uuid
from django.db import models
from django.conf import settings
from jsonfield import JSONField

# Class to get data after process algorithm and save to database
# REQUEST
class PlagiarismCheckRequest(models.Model):
    id = models.IntegerField(primary_key=True)
    sentence1 = models.TextField(blank=False, default="")
    sentence2 = models.TextField(blank=False, default="")
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)
    method = models.CharField(max_length=20)



# RESPONSE
class PlagiarismCheckResponse(models.Model):
    success = models.BooleanField(default=True)
    err_msg = models.TextField(blank=True, default="")
    id = models.IntegerField(primary_key=True)
    is_paraphrase = models.NullBooleanField()



# SAVE TO DB
class PlagiarismCheckSave(models.Model):
    id = models.AutoField(primary_key=True)
    input = JSONField(default="")
    output = JSONField(default="")
# Khi co loi phat sinh o request json, response json van chap nhan data de response

