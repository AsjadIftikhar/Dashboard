from django.contrib import admin
from .models import Jobs, Tasks, Instances, personData
# Register your models here.

admin.site.register(Tasks)
admin.site.register(Jobs)
admin.site.register(Instances)
admin.site.register(personData)