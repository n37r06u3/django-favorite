from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Favorite(models.Model):
    user = models.ForeignKey('auth.User')
    target_content_type = models.ForeignKey(ContentType)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'target_content_type', 'target_object_id'),)