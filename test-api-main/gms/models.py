from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission = models.BooleanField(default=None, null=True)


class Regions(models.Model):
    regions_name = models.CharField(max_length=100)
    regions_ref = models.CharField(max_length=100)

    def __str__(self):
        return self.regions_name

    class Meta:
        verbose_name_plural = 'Regions'


class Tenants(models.Model):
    tenants_name = models.CharField(max_length=100)
    tenants_ref = models.CharField(max_length=100)
    regionz = models.ManyToManyField(Regions)

    def __str__(self):
        return self.tenants_name

    class Meta:
        verbose_name_plural = 'Tenants'


class NameSpaces(models.Model):
    namespaces_name = models.CharField(max_length=100)
    namespaces_ref = models.CharField(max_length=100)
    tenantz = models.ManyToManyField(Tenants)
    files = models.FileField(upload_to='templates/themes/files/', null=True, blank=True)
    fileurl = models.URLField(default=None, null=True, blank=True)
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    def __str__(self):
        return self.namespaces_name

    class Meta:
        verbose_name_plural = 'NameSpaces'

    def save(self, *args, **kwargs):
        super(NameSpaces, self).save(*args, **kwargs)
        return self


class integerTable(models.Model):
    EP_CHOICES = (
        ("https://elasticbeanstalk-us-east-2-171683036970.s3.us-east-2.amazonaws.com/",
         "https://elasticbeanstalk-us-east-2-171683036970.s3.us-east-2.amazonaws.com/"),
    )
    AK_CHOICES = (
        ("AKIASP6I3H4VJMQDGZHG",
         "AKIASP6I3H4VJMQDGZHG"),
    )
    ASK_CHOICES = (
        ("uOwZp0GyHWFTrdZhnbb/6HZcrorwNnRKn6TDZfR3", "uOwZp0GyHWFTrdZhnbb/6HZcrorwNnRKn6TDZfR3"),
    )
    address = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    END_POINT = models.CharField(max_length=100, choices=EP_CHOICES, blank=True, null=True)
    Access_KEY = models.CharField(max_length=100, choices=AK_CHOICES, blank=True, null=True)
    Acess_Secret_key = models.CharField(max_length=100, choices=ASK_CHOICES, blank=True, null=True)

    regions = models.ForeignKey("Regions", on_delete=models.CASCADE)

    def __str__(self):
        return self.username
