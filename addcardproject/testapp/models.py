from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
from django.core.validators import RegexValidator
alphabets = RegexValidator(
    r'^[a-zA-Z]*$', 'Only alphabets characters are allowed.')


class Card(models.Model):
    image = models.ImageField(
        blank=True, upload_to='static/image')
    title = models.CharField(max_length=25, validators=[alphabets])

    description = models.CharField(max_length=500, validators=[
                                   alphabets, MinLengthValidator(25, 'the field must contain at least 25 characters')])

    def __str__(self):
        return self.title
