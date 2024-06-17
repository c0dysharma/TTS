import uuid
from django.db import models


class TransformationInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(null=False)
    s3_url = models.TextField(null=True)
    output_filepath = models.TextField(null=False)
    model_used = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Status(models.TextChoices):
        QUEUED = 'QUEUED'
        PROCESSING = 'PROCESSING'
        COMPLETED = 'COMPLETED'
        FAILED = 'FAILED'

    status = models.CharField(
        choices=Status.choices,
        default=Status.QUEUED,
    )
