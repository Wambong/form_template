from django.db import models


class FormTemplate(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    fields = models.JSONField(null=True, blank=True)


    def __str__(self):
        return self.name



