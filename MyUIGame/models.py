from django.db import models

# Create your models here.
# Create Attributes model


class Attribute(models.Model):
    name = models.CharField(max_length=255)
# Create Areas model

class Territory(models.Model):
    name = models.CharField(max_length=255)
        
# Create Genders model


class Gender(models.Model):
    name = models.CharField(max_length=255)

# Create Skills model


class Skill(models.Model):
    name = models.CharField(max_length=255)

# create Weapone_type model


class Weapone_type(models.Model):
    name = models.CharField(max_length=255)

# Create Weapons model


class Weapone(models.Model):
    name = models.CharField(max_length=255)
    weapone_type = models.ForeignKey(
        "Weapone_type", blank=True, null=True, on_delete=models.CASCADE)
# Create  Figures model


class Figure(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    attribute = models.ForeignKey(
        "Attribute", blank=True, null=True, on_delete=models.CASCADE)
    gender = models.ForeignKey(
        "Gender", blank=True, null=True, on_delete=models.CASCADE)
    territory = models.ForeignKey(
        "Territory", blank=True, null=True, on_delete=models.CASCADE)
    starts = models.IntegerField()
    image = models.CharField(max_length=255)


# Create Figures_skills model


class Figures_skill(models.Model):
    figure = models.ForeignKey(
        "Figure", blank=True, null=True, on_delete=models.CASCADE)
    skill = models.ForeignKey(
        "Skill", blank=True, null=True, on_delete=models.CASCADE)

# create Figures_weapons model


class Figures_weapon(models.Model):
    figure = models.ForeignKey(
        "Figure", blank=True, null=True, on_delete=models.CASCADE)
    weapon = models.ForeignKey(
        "Weapone", blank=True, null=True, on_delete=models.CASCADE)
