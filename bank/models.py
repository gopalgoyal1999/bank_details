from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)

    def __str__(self):
        return self.branch
