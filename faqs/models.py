from django.db import models

class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()