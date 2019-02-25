from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Race model
class Race(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


# Class model
class Class(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=100, blank=True)
    power_one = models.ForeignKey('ClassPower', on_delete=models.CASCADE, related_name='attack')
    power_two = models.ForeignKey('ClassPower', on_delete=models.CASCADE, related_name='heal')

    class Meta:
        verbose_name_plural = _("Classes")

    def __str__(self):
        return self.name


# Powers model
class ClassPower(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


# Character model
class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=14, unique=True, null=True)
    race = models.ForeignKey('Race', on_delete=models.CASCADE)

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    def custom_default(self):
        return ('{}.jpg'.format(self.race.name))

    image = models.ImageField(blank=True, default=0)
    char_class = models.ForeignKey('Class', on_delete=models.CASCADE)
    description = models.TextField(max_length=400, blank=True)
    enemy = models.ForeignKey('Enemy', on_delete=models.CASCADE, null=True)

    # Save images according to race gender
    def save(self, *args, **kwargs):

        if self.gender == self.GENDER_CHOICES[0][0]:
            self.image = '{}.jpg'.format(self.race.name.lower())
        else:
            self.image = '{}_female.jpg'.format(self.race.name.lower())

        # Save character name capitalized
        self.name = self.name.capitalize()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Enemy model
class Enemy(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, default=0)

    class Meta:
        verbose_name_plural = _("Enemies")

    def __str__(self):
        return self.name
