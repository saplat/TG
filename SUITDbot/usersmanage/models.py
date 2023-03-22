from django.db import models

# Create your models here.
class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class users(TimeBasedModel):
    fname = models.CharField(max_length=100, null=True)
    id_tg = models.BigIntegerField(unique=True, null=True)
    groupus = models.CharField(max_length=10, null=True)

class schedules(TimeBasedModel):
    group_user = models.CharField(max_length=10, null=True)
    dayi = models.IntegerField(null=True)
    schedule = models.CharField(max_length=1000, null=True)
    updown = models.IntegerField(null=True)

class teachers(TimeBasedModel):
    fname = models.CharField(max_length=100, null=True)
    dayi = models.IntegerField(null=True)
    schedule = models.CharField(max_length=1000, null=True)
    updown = models.IntegerField(null=True)