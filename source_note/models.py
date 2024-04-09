from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Section(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class Note(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False, related_name="associated_notes")
    title = models.CharField(max_length=100, null=True)
    extension = models.CharField(max_length=10, null=True)
    file = models.FileField(upload_to="uploads/notes/")

    def __str__(self):
        return self.title

