from django.db import models


class Equacao2Grau(models.Model):
    a = models.DecimalField(max_digits=10, decimal_places=4)
    b = models.DecimalField(max_digits=10, decimal_places=4)
    c = models.DecimalField(max_digits=10, decimal_places=4)
