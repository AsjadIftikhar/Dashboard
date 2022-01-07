# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class UserSpaces(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     space_url = models.URLField(blank=False)
#     space_type = models.IntegerField(max_length=256, choices=[(1, 'namespace'), (2, 'tenant')])
#     created_date = models.DateTimeField(auto_now=True)

#     def __unicode__(self):
#         return self.user.username+" "+self.space_url

#     class Meta:
#         verbose_name_plural = "User Spaces"