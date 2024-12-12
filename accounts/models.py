from django.db import models
from django.contrib.auth.models import User

SEXE = (
    ("M", "Masculin"),
    ("F", "Feminin")
)


class visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=15, choices=SEXE, blank=True, null=True)
    birthday = models.DateTimeField("birthday", blank=True, null=True)
    fonction = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
