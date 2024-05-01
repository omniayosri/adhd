from django.db import models
from django.contrib.auth.models import User

class DoctorProfile(models.Model):
    user = models.OneToOneField(User,
                                related_name='doctor',
                                on_delete=models.CASCADE
                                )
    
    def __str__(self) -> str:
        return f'Doctor {self.user}'