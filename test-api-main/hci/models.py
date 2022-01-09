from django.db import models


# Create your models here.

class Tasks(models.Model):
    displayName = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    progress = models.CharField(max_length=100)
    currentStep = models.IntegerField(default=0)
    totalStep = models.IntegerField(default=0)
    totalErrorCount = models.IntegerField(default=0)

    def __str__(self):
        return self.displayName

    class Meta:
        verbose_name_plural = 'Tasks'


class Jobs(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    currentStep = models.IntegerField(default=0)
    totalStep = models.IntegerField(default=0)
    steps = models.IntegerField(default=0)
    stepReports = models.IntegerField(default=0)
    totalErrorCount = models.IntegerField(default=0)
    serviceUnits = models.IntegerField(default=0)
    executionInstanceId = models.CharField(max_length=100)
    instanceMetrics = models.CharField(max_length=100)
    dueDate = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Jobs'


class Instances(models.Model):
    ipAddress = models.CharField(max_length=100)
    externalIpAddress = models.CharField(max_length=100)
    master = models.BooleanField(default=False)
    matrices = models.CharField(max_length=100)
    services = models.CharField(max_length=100)
    jobs = models.CharField(max_length=100)
    alerts = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    recommendedServiceUnits = models.IntegerField(default=0)
    allocatedServiceUnits = models.IntegerField(default=0)
    serviceUnitStatus = models.CharField(max_length=100)
    serviceUnitStatusMessage = models.CharField(max_length=100)

    def __str__(self):
        return self.ipAddress

    class Meta:
        verbose_name_plural = 'Instances'


class personData(models.Model):
    grant_type = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    adminPassword = models.CharField(max_length=100, null=True, blank=True)
    scope = models.CharField(max_length=100, null=True, blank=True)
    client_secret = models.CharField(max_length=100, null=True, blank=True)
    client_id = models.CharField(max_length=100, null=True, blank=True)
    realm = models.CharField(max_length=100, null=True, blank=True)
    template_query = models.FileField(upload_to='templates/themes/files/', null=True, blank=True)
    written_query = models.FileField(upload_to='templates/themes/files/', null=True, blank=True)
