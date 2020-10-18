# conversations/models.py
from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField("users.User", related_name="converstation", blank=True)


    def __str__(self):
        return self.created