from django.db import models


# Create your models here.
class MyModel(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=("id",))
        ]


class RelatedModel(models.Model):
    thing = models.ForeignKey(MyModel, on_delete=models.CASCADE, related_name="lol")
    many = models.ManyToManyField(MyModel, related_name="lol2")

    class Meta:
        indexes = [
            models.Index(fields=("thing",))
        ]
