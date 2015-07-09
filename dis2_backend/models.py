from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

class AppUser(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class School(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    sigil = models.ImageField(blank=True)

    members = models.ManyToManyField('AppUser', blank=True, related_name='schools')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    sigil = models.ImageField(blank=True)

    school = models.ForeignKey('School', related_name='groups')
    members = models.ManyToManyField('AppUser', blank=True, related_name='groups')

    def __str__(self):
        return self.name

class Event(models.Model):
    value = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    school = models.ForeignKey('School', related_name='events')
    students = models.ManyToManyField('AppUser', related_name='events')

    def __str__(self):
        return self.name


class Reward(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)

    school = models.ForeignKey('School', related_name='rewards')

    def __str__(self):
        return self.name


class Achievement(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    badge = models.ImageField(blank=True)

    students = models.ManyToManyField('AppUser', blank=True, related_name='achievements')

    def __str__(self):
        return self.name
