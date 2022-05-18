from django.db import models


class User(models.Model):

    cpf = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        primary_key=True
    )

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    birtday = models.DateField(
        null=False,
        blank=False
    )


class Salaries(models.Model):
    cpf = models.CharField(
        max_length=11,
        null=False,
        blank=False,
    )

    date = models.DateField(
        null=False,
        blank=False
    )

    salary = models.FloatField(
        null=False,
        blank=False
    )

    discount = models.FloatField(
        null=False,
        blank=False
    )
