from django.db import models

# Create your models here.
class Challenge(models.Model):
    writer = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(null=True)
    reward = models.CharField(max_length=200,null=True)
    types = models.CharField(max_length=200,null=True)
    usages = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title

class ChallengeFromHighhat(models.Model):
    title = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

class Addchallenge(models.Model):
    writer = models.CharField(max_length=200, null=True)
    music = models.CharField(max_length=1000, null=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.writer

class Sample(models.Model):
    title = models.CharField(max_length = 200, null=True)
    photo = models.ImageField(blank=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.summary[:30]