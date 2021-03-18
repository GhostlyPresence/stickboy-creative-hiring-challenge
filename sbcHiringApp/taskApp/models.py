from django.db import models
from django.contrib.auth.models import User
from taskApp.validators import schedule_validator as sv

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200, null=True)
    task_description = models.CharField(max_length=2000, null=True)
    start_date = models.DateField(auto_now_add=False, null=False)
    end_date = models.DateField(auto_now_add=False, null=False)

    def __str__(self):
        return str(self.name)
    
class Schedule(models.Model):
    task_name = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
    employee = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    start_time = models.DateTimeField(validators=[sv.validate_start_date_time])
    end_time = models.DateTimeField(validators=[sv.validate_end_date_time])

    def __str__(self):
        return str(self.task_name)




