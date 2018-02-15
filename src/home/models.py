# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registration(models.Model):
	institute_name = models.CharField(null=False, blank=False,max_length=60)
	student_name = models.CharField(null=False, blank=False,max_length=25)
	secratary_name = models.CharField(null=False, blank=False,max_length=25)
	incharge_name = models.CharField(null=False, blank=False,max_length=25)
	cricket_boys = models.BooleanField(default=False)
	football_boys = models.BooleanField(default=False)
	basketball_boys = models.BooleanField(default=False)
	volleyball_boys = models.BooleanField(default=False)
	squash_boys = models.BooleanField(default=False)
	lawn_tennis_boys = models.BooleanField(default=False)
	badminton_boys = models.BooleanField(default=False)
	atheletics_boys = models.BooleanField(default=False)
	triathlon_boys = models.BooleanField(default=False)
	table_tennis_boys = models.BooleanField(default=False)
	swimming_boys = models.BooleanField(default=False)
	carrom_boys = models.BooleanField(default=False)
	chess_boys = models.BooleanField(default=False)
	basketball_girls = models.BooleanField(default=False)
	volleyball_girls = models.BooleanField(default=False)
	squash_girls = models.BooleanField(default=False)
	lawn_tennis_girls = models.BooleanField(default=False)
	badminton_girls = models.BooleanField(default=False)
	atheletics_girls = models.BooleanField(default=False)
	triathlon_girls = models.BooleanField(default=False)
	table_tennis_girls = models.BooleanField(default=False)
	swimming_girls = models.BooleanField(default=False)
	carrom_girls = models.BooleanField(default=False)
	chess_girls = models.BooleanField(default=False)
	email = models.CharField(null=False, blank=False,max_length=25)
	faculty_email = models.CharField(null=False, blank=False,max_length=25)
	phone_number = models.CharField(null=False, blank=False,max_length=25)
	secratary_phone_number = models.CharField(null=False, blank=False,max_length=25)