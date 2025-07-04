from django.db import models

# Create your models here.


class CreateForm(models.Model):
    question = models.CharField(max_length=200)
    option_One = models.CharField(max_length=50)
    option_one_count = models.IntegerField(default=0,editable=False)
    option_Two = models.CharField(max_length=50)
    option_two_count = models.IntegerField(default=0,editable=False)

    option_Three = models.CharField(max_length=50)
    option_three_count = models.IntegerField(default=0,editable=False)
