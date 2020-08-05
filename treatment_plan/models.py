import os
import uuid

from django.db import models   
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def get_upload_path(instance, filename):
    '''
    Function that takes in an instance and returns the path
    to upload files to.
    '''
    if instance.resource_type == "VD":
        return f'treatment_plan/static/treatment_plan/external_resources/{instance.clientPresentation.id}/videos/{filename}'
    else:
        return f'treatment_plan/static/treatment_plan/external_resources/{instance.clientPresentation.id}/documents/{filename}'

class ClientPresentation(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if other != None:
            if isinstance(other, str):
                return self.name == other
            elif isinstance(other, ClientPresentation):
                return self.name == other.name
        return False

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.name < other.name

    def __hash__(self):
        return hash(self._get_pk_val())

class Treatment(models.Model):
    OBSERVATION = "OB"
    LONG_TERM_GOAL = "LT"
    SHORT_TERM_OBJECTIVE = "ST"
    THERAPEUTIC_INTERVENTION = "TI"
    CLIENT_PROGRESS = "CP"
    PLAN = "PL"
    TREATMENT_TYPE_CHOICES = [
        (OBSERVATION, "Observation/Assessment"),
        (LONG_TERM_GOAL, "Long Term Goal"),
        (SHORT_TERM_OBJECTIVE, "Short Term Objective"),
        (THERAPEUTIC_INTERVENTION, "Therapeutic Intervention"),
        (CLIENT_PROGRESS, "Client Progress"),
        (PLAN, "Plan for Next Session")
    ]

    treatment_type = models.CharField(
        max_length=2,
        choices=TREATMENT_TYPE_CHOICES,
        default=OBSERVATION)
    description = models.TextField()
    clientPresentation = models.ForeignKey(ClientPresentation, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def __eq__(self, other):
        if other != None:
            if isinstance(other, str):
                return self.description == other
            elif isinstance(other, ClientPresentation):
                return self.description == other.description
        return self.description == other.description

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.description < other.description

    def __hash__(self):
        return hash(self._get_pk_val())

class ExternalResource(models.Model):
    VIDEO = "VD"
    DOCUMENT = "DT"
    RESOURCE_TYPE_CHOICES = [
        (VIDEO, "Video"),
        (DOCUMENT, "Document")
    ]
    name = models.TextField()
    resource_type = models.CharField(
        max_length=2,
        choices=RESOURCE_TYPE_CHOICES,
        default=VIDEO)
    clientPresentation = models.ForeignKey(ClientPresentation, on_delete=models.CASCADE)
    path = models.FileField(upload_to=get_upload_path, blank=True)
    URL = models.TextField(blank=True)

    def clean(self):
        #Only allow one value to be blank between path and URL
        if self.path == "" and self.URL == "":
            raise ValidationError(_('Path or URL must be filled. '))
        elif self.path != "" and self.URL != "":
            raise ValidationError(_('Only one of Path and URL can be filled. '))

    def __str__(self):
        return f'{self.resource_type }: {self.name} ({self.clientPresentation.name})'

@receiver(models.signals.post_delete, sender=ExternalResource)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding 'ExternalResource' object is deleted.
    """

    # instance.path is the field 'path' and the following
    # .path is for the file's path attribute 
    if instance.path:
        if os.path.isfile(instance.path.path):
            os.remove(instance.path.path)

@receiver(models.signals.pre_save, sender=ExternalResource)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding 'ExternalResource' object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = ExternalResource.objects.get(pk=instance.pk).path
    except ExternalResource.DoesNotExist:
        return False

    new_file = instance.path
    if old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)