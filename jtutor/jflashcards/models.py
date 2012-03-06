from django.db import models

class Clue(models.Model):
  category = models.CharField(max_length=100)
  correct_response = models.CharField(max_length=100)
  game = models.CharField(max_length=100)
  value = models.IntegerField()
  clue = models.CharField(max_length=1000)

class Response(models.Model):
  clue = models.ForeignKey(Clue)
  correct = models.BooleanField()
  knew = models.NullBooleanField()
  heardof = models.NullBooleanField()
  response_time = models.DateTimeField('response time')
