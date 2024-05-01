from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User,
                                related_name='patient',
                                on_delete=models.CASCADE
                                )
    

    def __str__(self) -> str:
        return f'Patient {self.user}'