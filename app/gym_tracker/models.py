from django.db import models


class Weigh_In(models.Model):
    date = models.DateField()
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=2, decimal_places=2)
    muscle_mass = models.DecimalField(max_digits=3, decimal_places=2)

class Lift_Type(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateField()
    max_weight = models.DecimalField(max_digits=3, decimal_places=2)

class Member(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = models.IntegerField(max_length=10)
    email = models.CharField(max_length=200)
    # foreign key - weigh_in
    weigh_in = models.ForeignKey(Weigh_In, null=True)
    # foreign key - lift_type
    lift_type = models.ForeignKey(Lift_Type, null=True)

class Coach(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)

class Movement(models.Model):
    name = models.CharField(max_length=70)
    reps = models.IntegerField(max_length=3, null=True)
    time = models.TimeField(null=True)

class Workout(models.Model):
    name = models.CharField(max_length = 200)
    date = models.DateField()
    # Many-to-many relationships
    movement = models.ManyToManyField(Movement)
    coach = models.ManyToManyField(Coach)