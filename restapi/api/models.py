# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    profileUrl = models.CharField(max_length = 100)

    class Meta:
        db_table = u't_person'

    def __str__(self):
        return "{},{}".format(self.name, self.email)

class Presentation(models.Model):
    id = models.CharField(max_length = 50, primary_key = True)
    title = models.CharField(max_length = 100)
    creator = models.ForeignKey(Person, on_delete=models.CASCADE,)
    createdAt = models.DateField()
    thumbnailUrl = models.CharField(max_length = 100)

    class Meta:
       db_table = u't_presentation'
       ordering = ('id',)
