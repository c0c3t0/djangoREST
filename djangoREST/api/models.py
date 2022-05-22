from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    NAME_MAX_LEN = 25
    PRICE_MIN_VALUE = 0.01

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )
