from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    dob = models.DateField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.name
