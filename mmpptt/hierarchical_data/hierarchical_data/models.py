# using this tutorial: https://django-mptt.readthedocs.io/en/latest/tutorial.html
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


type_of_choices = (
    ('folder', 'Folder'),
    ('file', 'File'),
)


class File(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    type_of = models.CharField(
        max_length=6, choices=type_of_choices, default='file')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
