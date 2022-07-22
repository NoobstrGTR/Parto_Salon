from django.db import models
from django.core.validators import int_list_validator, MinLengthValidator
from django.utils.translation import gettext_lazy as _
from user.models import UserProfileModel

# Create your models here.
class ServicesModel(models.Model):
    servics = models.CharField(max_length=200)

    def __str__(self):
        return self.servics


class DescriptionModel(models.Model):
    service = models.ForeignKey(ServicesModel, on_delete=models.CASCADE)
    description = models.TextField(null= True, blank=True)
    price = models.FloatField(blank=False, null=False)
    time_minutes = models.IntegerField(blank=False, null=False)

    def __str__(self):
            return f'{self.service} {self.price}'

class Appointment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    customer = models.ForeignKey(
        UserProfileModel, related_name='customer', on_delete=models.CASCADE, blank=False, null=False)
    employee = models.ForeignKey(
        UserProfileModel, related_name='employee', on_delete=models.CASCADE, blank=False, null=False)
    services = models.CharField(max_length=1000, validators=[
                                int_list_validator], blank=False, null=False)  # list of comma seperated service id's [3, 5]

    def __str__(self):
        return f'StartTime={self.start_time} | EndTime={self.end_time} | Employee={self.employee} | Customer={self.customer}'

    class Meta:
        ordering = ['start_time']
        

class PastAppointment(models.Model):
    created = models.DateTimeField(blank=False, null=False)
    appointment_id = models.IntegerField(blank=False, null=False)
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField(blank=False, null=False)
    customer = models.ForeignKey(UserProfileModel, related_name='past_appointment_customer',
                                 on_delete=models.CASCADE, blank=False, null=True)
    employee = models.ForeignKey(UserProfileModel, related_name='past_appointment_employee',
                                 on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return f'StartTime={self.start_time} | EndTime={self.end_time} | Employee={self.employee} | Customer={self.customer}'

    class Meta:
        ordering = ['start_time']